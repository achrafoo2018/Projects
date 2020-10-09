@extends('layouts.app')

@section('title')
    <title>Post</title>
@stop
@section('content')
    <h1>Post {{$result->title}}</h1>
    <p>Content: {{$result->content}}</p>
@stop
