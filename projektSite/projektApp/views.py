from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Autor, Gatunek, Book, Borrow
from .serializers import AutorSerializer, GatunekSerializer, BookSerializer, BorrowSerializer
from .forms import RegisterForm


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


def index(request):
    return HttpResponse("Hello World?")


@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def autorzy_list(request):
    if request.method == 'GET':
        autorzy = Autor.objects.all()
        serializer = AutorSerializer(autorzy, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def autorzy_detail(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)


@api_view(['GET'])
def autorzy_string(request, string):
    if request.method == 'GET':
        autor = Autor.objects.filter(nazwisko__contains=string) | \
                Autor.objects.filter(imie__contains=string)
        serializer = AutorSerializer(autor, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_required('projektApp.change_autor', 'projektApp.delete_autor')
def autorzy_update_delete(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_required('projektApp.add_autor')
def autorzy_post(request):
    if request.method == 'GET':
        autorzy = Autor.objects.all()
        serializer = AutorSerializer(autorzy, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def gatunki_list(request):
    if request.method == 'GET':
        gatunki = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunki, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def gatunki_detail(request, pk):
    try:
        gatunek = Gatunek.objects.get(pk=pk)
    except Gatunek.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GatunekSerializer(gatunek)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_required('projektApp.change_gatunek', 'projektApp.delete_gatunek')
def gatunki_update_delete(request, pk):
    try:
        gatunek = Gatunek.objects.get(pk=pk)
    except Gatunek.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GatunekSerializer(gatunek)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = GatunekSerializer(gatunek, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gatunek.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_required('projektApp.add_gatunek')
def gatunki_post(request):
    if request.method == 'GET':
        gatunki = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunki, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GatunekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def books_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


@api_view(['GET'])
def books_autor(request, string):
    if request.method == 'GET':
        book = Book.objects.filter(autor__nazwisko__contains=string) | \
               Book.objects.filter(autor__imie__contains=string)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def books_string(request, string):
    if request.method == 'GET':
        book = Book.objects.filter(nazwa__contains=string)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def books_gatunek(request, string):
    if request.method == 'GET':
        book = Book.objects.filter(gatunek__nazwa__contains=string)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_required('projektApp.change_book', 'projektApp.delete_book')
def books_update_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_required('projektApp.add_book')
def books_post(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def borrows_list(request):
    if request.method == 'GET':
        borrows = Borrow.objects.all()
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def borrows_detail(request, pk):
    try:
        borrow = Borrow.objects.get(pk=pk)
    except Borrow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowSerializer(borrow)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def borrows_konto(request, string):
    if request.method == 'GET':
        borrows = Borrow.objects.filter(konto__username__contains=string)
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def borrows_active(request):
    if request.method == 'GET':
        borrows = Borrow.objects.filter(data_zwrotu__isnull=True)
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def borrows_update_delete(request, pk):
    try:
        borrow = Borrow.objects.get(pk=pk)
    except Borrow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowSerializer(borrow)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BorrowSerializer(borrow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        borrow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def borrows_post(request):
    if request.method == 'GET':
        borrows = Borrow.objects.all()
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BorrowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('/app/books/')
        return render(request, 'users/register.html', {'form': form})
