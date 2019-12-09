# Projeto de Detecção de Fakenews
Trabalho da matéria de programação web 2019-2
- Caio Massucato 
- Diego Barbosa 
- Gabriel Martins 
- Matheus Rodrigues

## Objetivos
Esse projeto teve como objetivo a utilização de um modelo de Inteligência Artificial já existente para detectar notícias falsas. Além disso a integração desse modelo com um sistema web onde um usuário seja capaz de digitar uma notícia, em inglês, e checar a veracidade da mesma.


## Conjunto de dados utilizados
Utilizamos um arquivo com extensão *csv* composto por 6.335 notícias em inglês, sendo 3.171 classificadas como verdadeiras e 3.164 como falsas.

## Modelo da Rede Neural utilizado
Utilizamos como referência o modelo disponibilizado no repositório: *https://github.com/lutzhamel/fake-news*. Neste link é mostrado 2 modelos com abordagens distintas: o primeiro utiliza uma rede Bayesiana e o segundo uma rede Convolucional. No link: *https://github.com/dieg0D/Fakenews-Detection*, na *branch* *master* temos apenas o código que faz o treinamento da Rede Neural. Já na *branch* django temos o modelo já treinado que é utilizado sob a notícia digitada pelo usuário. No projeto da disciplina escolhemos o segundo por ter uma acurácia maior.

## Referências
- Blog que mostra informações (dataset, explicações das técnicas aplicadas, etc...) do modelo criado: https://www.kdnuggets.com/2017/04/machine-learning-fake-news-accuracy.html
- Repositório do modelo utilizado: https://github.com/lutzhamel/fake-news/blob/master/report.md