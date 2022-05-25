import 'package:flutter/material.dart';

void main(){
  //rodar app ou classe do app
  runApp(TelaInicial());

}

class TelaInicial extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Um texto filosófico", //Texto da aba no navegador
      home: Scaffold(
        appBar: AppBar(
          title: Text("Bem dinâmico"),
        ),

        body: Center(
          child: Text("Outro texto filosófico"),


        ),
        //Floating action button aqui
        floatingActionButton: FloatingActionButton(
          onPressed:(){
            print('Você apertou o botão');
          },
          backgroundColor: Colors.greenAccent,
          child:  Icon(Icons.save),

        ),

      ),
    );
  }


}