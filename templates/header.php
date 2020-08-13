<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <!--Mobile responsivness.-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <!--Grid layout-->
  <link rel="stylesheet" href="../static/vendors/css/grid.css">
  <!--Bootstrap-->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp"
    crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB"
    crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="../static/css/style.css">
  <title>Auto Body Template</title>
  <link rel="icon" href="../static/img/tab-logo.png">
</head>

<body>
  <!-- Navbar with dropdown. -->
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark sticky-top">
    <div class="container">
        <a class="navbar-brand" href="index.php" class="nav-text"><img class="logo-header" src="../static/img/full-logo.svg"/></a>

      <!--Mobile friendly menu-->>
      <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
      </button>
        <div  class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                  <a class="nav-link text-white navbar-link" href="index.php">Home</a>
              </li>
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle text-light" data-toggle="dropdown" href="#">Services</a>
                  <div class="dropdown-menu">
                    <a href="collision.php" class="dropdown-item nav-text"> Collision Repair</a>
                    <a href="refining.php" class="dropdown-item nav-text"> Automotive Refining</a>
                    <a href="mechanical.php" class="dropdown-item nav-text"> Mechanical Services</a>
                    <a href="#" class="dropdown-item nav-text"> Towing</a>
                </div>
              </li>
              <li class="nav-item">
                  <a class="nav-link nav-text text-light" href="#" data-toggle="modal" data-target="#exampleModal">Contact</a>
              </li>
              
          </ul>
          
        </div>
    </div>

    
</nav>

<!-- Contact Forum -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Having car issues? Let us help!</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                    </div>
                    <div class="modal-body">
                        <form action="/action_page.php">
                            <div class="row">
                                <input type="text" class="ml-3 mr-1 form-control col" placeholder="first name" id="first_name">
                                <input type="text" class=" mr-3 ml-1 form-control col" placeholder="last name" id="last _name">
                            </div>
                            
                            <div class="form-group mt-2">
                                <input type="email" class="form-control" placeholder="example@email.com" id="email">
                            </div>

                            <div class="form-group mt-2">
                                <input type="text" class="form-control" placeholder="phone number" id="phone number">
                            </div>

                            <div class="form-group">
                              <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="vehicle details">
                            </div>

                            <divn class="form-group mt-2">
                                <textarea class="form-control" aria-label="With textarea"></textarea>
                            </div>

                            <div class="d-flex justify-content-center mb-3">
                                <button type="button" class="btn btn-primary submit-btn" data-dismiss="modal">submit</button>
                            </div>
                        </form>
                    </div>  
                </div>
                </div>
