---
content_hash: 658c99a83095638d82fe453b220b7edfa156b81f6123a33b2be93a982dfde30b
fetched_at: '2026-06-29T00:10:26.756876+00:00'
page_id: '514731269'
product: rm
source: tdn-rm
title: Publicação do ambiente TReports Demo em ambiente Kubernetes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514731269
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | Todos |
| Segmento: | Todos |
| Módulo: | TReports |

## **02. SITUAÇÃO/REQUISITO**

Detalhamos através desse documento os principais procedimentos para publicação do TReports Demo em ambiente Kubernetes do TKS.

Pré-requisitos:

1) - Para execução desse procedimento, a máquina deverá possuir obrigatoriamente o sistema operacional windows 10 - Pro ou superior.

2) Instalar a última versão do docker ce;

3) - Verificar se o utilitário "MSBuild.exe" está localizado no caminho: C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\MSBuild\15.0\Bin\MSBuild.exe.

Se não estiver nesse caminho, o script "dockerdemopush.bat" deverá ser alterado de acordo com o novo caminho em questão. Esse comando é necessário para publicação do TReports.demo.

## **03. SOLUÇÃO**

**Passo a passo para publicação da imagem do TReports demo no docker.totvs**

1. Efetuar Get na solution do TReports disponibilizada no TFS no caminho : $/RM/Atual/Release/Core/TRF/TReports
2. Executar o arquivo bat "dockerdemopush.bat" localizado em: "$/RM/Atual/Release/Core/TRF/TReports";.

Obs: Esse script compila e publica o projeto "TRF.Rpt.WebApp.Demo" no diretório "TReportsDemo" e também gera e publica a imagem "treports\_demo:tag" no docker.totvs.

**Preparação do Kubernets:**

1. Abrir o power shell e acessar o diretório: "C:\RM\Atual\Release\Core\TRF\TReports\demo\TRF.Rpt.WebApp.Demo\Kubernets";
2. Rodar os comandos abaixo para limpeza do cluster:  
   kubectl --kubeconfig equipe-framework-treportsdemo-user delete deployment/treportsdemo  
   kubectl --kubeconfig equipe-framework-treportsdemo-user delete deployment/treportsdemodb  
   kubectl --kubeconfig equipe-framework-treportsdemo-user delete deployment/treportsdemoprovsample  
   kubectl --kubeconfig equipe-framework-treportsdemo-user delete service/svc-treportsdemo  
   kubectl --kubeconfig equipe-framework-treportsdemo-user delete service/svc-treportsdemodb  
   kubectl --kubeconfig equipe-framework-treportsdemo-user delete service/svc-treportsdemoprovsample

3) - Rodar os comando abaixo para carregar os pod's do banco de dados, demo e provedor samples  
   kubectl --kubeconfig equipe-framework-treportsdemo-user apply -f Db  
   kubectl --kubeconfig equipe-framework-treportsdemo-user apply -f Demo  
   kubectl --kubeconfig equipe-framework-treportsdemo-user apply -f ProvSample

## **04. DEMAIS INFORMAÇÕES**

* O container do TReports Demo será publicado na porta: 80;
* Os arquivos "hosting.json" localizado em "C:\RM\Atual\Release\Core\TRF\TReports\demo\TRF.Rpt.WebApp.Demo" e   
  "appsettings.prod.js" localizado em C:\RM\Atual\Release\Core\TRF\TReports\demo\TRF.Rpt.WebApp.Demo\ClientApp\src\assets  
  devem apontar para a porta 80.
* No arquivo "Dockerfile" deve existir a linha: EXPOSE 80 para o container expor essa porta.

As imagens congeladas do provedor sample e banco de dados já estão disponibilizados no docker.totvs:  
[docker.totvs.io/treports/treports\_demo\_provsample:12126](http://docker.totvs.io/treports/treports_demo_provsample:12126)  
[docker.totvs.io/treports/treports\_demo\_db:12126](http://docker.totvs.io/treports/treports_demo_db:12126)
