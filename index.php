<?php include 'header.php'; ?>

<!--Slide show that shows an images for collision repairs, mechanical services, and automotive refinishing.-->
<section id="showcase">
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li class="active" data-target="#myCarousel" data-slide-to="0"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <!--Image 1-->
    <div class="carousel-inner">
      <div class="carousel-item carousel-image-1 active">
        <div class="container">
          <div class="carousel-caption d-none d-sm-block text-right">
            <h1 class="display-3 slide-title">Heading one</h1>
          </div>
        </div>
      </div>

    <!--Image 2-->
      <div class="carousel-item carousel-image-2">
        <div class="container">
          <div class="carousel-caption d-none d-sm-block">
            <h1 class="display-3 slide-title">Heading Two</h1>
          </div>
        </div>
      </div>

    <!--Image 3-->
      <div class="carousel-item carousel-image-3">
        <div class="container">
          <div class="carousel-caption d-none d-sm-block text-right">
            <h1 class="display-3 slide-title mt-5">Heading Three</h1>
          </div>
        </div>
      </div>
  </div>

<a href="#myCarousel" data-slide="prev" class="carousel-control-prev">
        <span class="carousel-control-prev-icon"></span>
      </a>

      <a href="#myCarousel" data-slide="next" class="carousel-control-next">
        <span class="carousel-control-next-icon"></span>
      </a>
</section>

<!--Section showing icons for certified mechanics, lifetime warranty, satisfaction guaranteed.-->
<section class="icons m-auto">
  <div class="icons-container">
    <div class="selling-point-container row"> 
        <h2 class="m-auto section-title">The best collision repair center in Rockville</h2>
        <p class="selling-point m-auto pt-5">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati illum incidunt omnis labore officiis 
            facere praesentium corporis, quo blanditiis placeat laudantium accusamus harum facilis veritatis minus 
            quibusdam repellendus quisquam aspernatur.  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati illum incidunt omnis labore officiis 
            facere praesentium corporis, quo blanditiis placeat laudantium accusamus harum facilis veritatis minus 
            quibusdam repellendus quisquam aspernatur.
        </p>
    </div>
  </div>
</section>

 <!-- SCROLLING IMAGE SECTION -->
  <section id="scrolling-image" class="bg-dark p-5">
    <div class="dark-overlay">
      <div class="row">
        <div class="col">
          <div class="container">
            <div class="row">
              <div class="col span-1-of-3 icon-container" id="tech-container">
                  <ion-icon name="build" class="build-icon" id="build-icon"></ion-icon>
                  <h3 class="icon-title text-white">Certified Technitions</h3>
                  <p class="icon-description text-white" id="icon-description-1">Lorem ipsum dolor sit amet consectetur adipisicing elit. In, eligendi excepturi doloribus 
                    cupiditate dolorum aut tempore quia numquam fugit enim adipisci voluptate, hic sed error laborum 
                    quidem iste praesentium magni!</p>
              </div>
              
              <div class="col span-1-of-3 icon-container" id="car-container">
                  <ion-icon name="car" class="car-icon" id="car-icon"></ion-icon>
                  <h3 class="icon-title text-white">Body Repair</h3>
                      <p class="icon-description text-white" id="icon-description">Lorem ipsum dolor sit amet consectetur adipisicing elit. In, eligendi excepturi doloribus 
                        cupiditate dolorum aut tempore quia numquam fugit enim adipisci voluptate, hic sed error laborum 
                        quidem iste praesentium magni!</p>
              </div>
             
              <div class="col span-1-of-3 icon-container" id="calendar-container">
                <ion-icon name="calendar" class="calandar-icon" id="calendar-icon"></ion-icon>
                <h3 class="icon-title text-white">Lifetime Guarantee</h3>
                  <p class="icon-description text-white" id="icon-description">Lorem ipsum dolor sit amet consectetur adipisicing elit. In, eligendi excepturi doloribus 
                  cupiditate dolorum aut tempore quia numquam fugit enim adipisci voluptate, hic sed error laborum 
                  quidem iste praesentium magni!</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

<!--Get an estimate form-->
<section class="get-an-estimate row m-auto">
      <div class="col span-1-of-2 estimate-container">
          <h3 class="section-title estimate-title">Get An Estimate Today</h3>
          <p class="estimate-description">Lorem ipsum dolor sit amet consectetur adipisicing elit. In, eligendi excepturi doloribus 
          cupiditate dolorum aut tempore quia numquam fugit enim adipisci voluptate, hic sed error laborum 
          quidem iste praesentium magni! Lorem ipsum dolor sit amet consectetur adipisicing elit. In, eligendi excepturi doloribus 
          cupiditate dolorum aut tempore quia numquam fugit enim adipisci voluptate, hic sed error laborum 
          quidem iste praesentium magni!</p>
      </div>

      <div class="estimate-form mg-auto col span-2-of-2" >
            <div class="card border-dark text-center card-form max-width:18rem">
              <div class="card-body">
                <h3 class="card-header text-dark">Collision Repair</h3>
                <form method="POST">
                  <div class="form-group">
                  <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="full name">
                  </div>

                  <div class="form-group">
                  <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="example@email.com">
                  </div>

                  <div class="form-group">
                  <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="phone number">
                  </div>

                  <div class="form-group">
                  <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="vehicle details">
                  </div>

                  <div class="form-group">
                  <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="problem description">
                  </div>
                  <button type="button" class="btn btn-outline-primary">Submit</button>
                </form>
              </div>
            </div>
          </div>
        </section>

<!-- Show location using google maps API-->
<section class="location m-auto">

  <div id = "location-contents" class="location-contents row">

    <div id = "location-information" class="location-information col span-1-of-2">
      <h3 class="section-title location-title">Rockville, MD</h3>
      <p id="location-description"class="location-description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo hic
         excepturi aperiam rerum. Earum porro repellendus cumque. Nisi voluptates, obcaecati repudiandae 
         ipsa illo animi iste dolor dolores similique placeat maiores! Lorem ipsum dolor sit amet, consectetur 
         adipisicing elit. Quo, corporis. Ipsam maxime magni ullam vero repellat, suscipit iure, quibusdam dignissimos 
         voluptatem quod at sed fugit inventore. Inventore quis expedita rerum.</p>
    </div>
    
    <div class="col span-1-of-2 mr-3">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d49549.683914086505!2d-77.18125395091283!3d39.086994858622376!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b62a2cfee39115%3A0xeca5be10d9c9df24!2sRockville%2C%20MD!5e0!3m2!1sen!2sus!4v1597278042671!5m2!1sen!2sus" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    </div>
  </div>

</section>

<?php include 'footer.php'; ?>
