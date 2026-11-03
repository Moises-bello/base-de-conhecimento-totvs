---
content_hash: c735e5438ee665b4fe06c008bb304db0f76626e9dd091d40ca35be7763c1570b
fetched_at: '2026-06-29T00:11:46.608474+00:00'
page_id: '823303856'
product: rm
source: tdn-rm
title: Integração Imagem Carestream
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=823303856
version: 13
---

## 

## **CONTEÚDO**

PainelVisão Geral

## **VISÃO GERAL**

Esta integração é utilizada para fazer a importação de arquivos PDF de resultado Carestream para o sistema.

Configuração

## **01. CONFIGURAÇÃO**

Integração tanto para Resultados de Imagem quanto para Laboratorial.

Configure o parâmetro geral: 

Saúde > Hospitais e Clinicas > Ambiente > Parâmetros > Gestão Hospitalar.

As opções que serão exibidas são essas, então basta seguir o fluxo:  
  
Unidades Diagnóstico > Integrações > Diagnóstico por Imagem > Carestream.

A tela que irá aparecer é essa:

A opção diretório não apresenta nenhuma alternativa para edição por ela agora pois os valores padrões pré-definidos,  a opção WebService irá habilitar os campos de Endereço, Método, Usuário e Senha para preenchimento.

Configure segundo a sua utilização para Imagem ou Laboratório utilizando "Carestream, Philips, Tuxxon, Pixeon" para Imagem ou "Matrix, TCM-EV, Shift, AgileWokr" para Laboratório preenchendo as informações corretas que se pedem nos respectivos campos.

Após vai em: Cadastros > Uso Geral > Unidades de Atendimento >> Selecione a unidade de atendimento e de um duplo click > Aba Integrações

selecione respectivamente as suas configurações para Imagem ou Laboratório. 

Usabilidade

## **02. USABILIDADE**

Selecione a unidade de diagnostico desejada em  ou  [Nesse caso usamos Laboratório]

Selecione o exame desejado usando o ChekBox conforme imagem abaixo.

2
complete
Exame Desejado

Processos > Integração Laboratorial e de Imagem - vide imagem abaixo

Será exibido a seguinte tela:

Clique em "Executa Integração"

É exibido a seguinte mensagem caso esteja tudo configurado corretamente.

A coluna "status" muda para o check marcado.

Se não exibe a seguinte mensagem

A coluna "status" desmarca o check 

Processo Manual 

## **03.** **PROCESSAMENTO MANUAL DE ARQUIVOS DE RESULTADO**

**Atenção: O processamento manual de arquivos foi alterado a partir da versão 2502, no qual agora segue os padrões da .**

Para realizar a integração de arquivos PDF de resultados manualmente (Exemplo: Laudos)

acesse **Utilitários > Rotinas > Processamento Manual de Arquivos de Integração**

Selecione a pasta que contém o arquivo PDF de resultado.

O arquivo deve possuir como nome o ACCESSION NUMBER:   
1 + Número da Ordem de Serviço (exemplo: 148527) + 1 => **11485271.pdf**

**Após executar o processo:**

**E o status do Laudo ficará como LIBERADO e o PDF ficará salvo no banco de dados.**

Para abrir o Resultado PDF pelo **RM**, na tela de Laudos acesse **Anexos > Arquivos**

Selecione o Arquivo e clique em **Visualizar Arquivo Selecionado**

E um PDF será criado e aberto.  
  
Para abrir o Resultado PDF pelo **PEP**, acesse o **PEP > Pacientes** e pesquise o paciente.

Acesse **Resultado de Exames**

**1** – Em **Documentos anexados ao prontuário** é possível ver os documentos anexados ao pedido e visualizar o PDF de resultado.

2 – Ao clicar na seta do Exame, é possível visualizar o PDF de resultado atrelado a ele.

Clique em **Visualizar** e o arquivo PDF será aberto.

ArquivoIdArquivo

**ARQUIVOS:**

1) Envio (Totvs) de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Requisicao;**
  + Nome do arquivo segue o seguinte padrão:
    - código da coligada + número do pedido de exame + Sequencia exame + ".xml"
    - Exemplo: 11490061.xml
  + Conteúdo:

| *<?xml version="1.0" encoding="ISO-8859-1"?> <MWL\_ITEM>   <ACTION>SAVE</ACTION>   <WS\_UID>11490061</WS\_UID>   <SITE>CENTRO CIRÚRGICO</SITE>   <PATIENT\_ID>50194</PATIENT\_ID>   <PATIENT\_NAME>JOAO JOSE</PATIENT\_NAME>   <PATIENT\_BIRTHDATE>19601108</PATIENT\_BIRTHDATE>   <PATIENT\_SEX>M</PATIENT\_SEX>   <PATIENT\_EMAIL\_CONSENT>N</PATIENT\_EMAIL\_CONSENT>   <PATIENT\_LOCATION>Andar: 2 - 236-3</PATIENT\_LOCATION>   <ACCESSION\_NUMBER>11490061</ACCESSION\_NUMBER>   <REFERRING\_PHYSICIAN>Dr Matheus</REFERRING\_PHYSICIAN>   <REFERRING\_PHYSICIAN\_IDENTIFICATION>64004</REFERRING\_PHYSICIAN\_IDENTIFICATION>   <REQUESTING\_DEPARTMENT>CENTRO CIRÚRGICO</REQUESTING\_DEPARTMENT>   <MODALITY>US</MODALITY>   <REQUESTED\_PROCEDURE\_DESCRIPTION>RX - ABDOMEN SIMPLES - A.P. - 40808017</REQUESTED\_PROCEDURE\_DESCRIPTION>   <SCHEDULED\_PERFORMING\_PHYSICIAN>   </SCHEDULED\_PERFORMING\_PHYSICIAN>   <SCHEDULED\_STATION\_AE\_TITLE>   </SCHEDULED\_STATION\_AE\_TITLE>   <SCHEDULED\_PROCEDURE\_STEP\_ID>1</SCHEDULED\_PROCEDURE\_STEP\_ID>   <DATE>20250211</DATE>   <TIME>084913</TIME>   <REQUESTED\_PROCEDURE\_ID>30011</REQUESTED\_PROCEDURE\_ID> </MWL\_ITEM>* |
| --- |

2) Envio (Totvs) de cancelamento de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Requisicao;**
  + Nome do arquivo segue o seguinte padrão:
    - del + código da coligada + número do pedido de exame + Sequencia exame + ".xml"
    - Exemplo: del11490061.xml

* + Conteúdo:

| *<?xml version="1.0" encoding="ISO-8859-1"?> <MWL\_ITEM>   <ACTION>DELETE</ACTION>   <WS\_UID>11490061</WS\_UID>* *</MWL\_ITEM>* |
| --- |

3) Resposta (Carestream) em XML de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Requisicao\Resposta;**
  + Nome do arquivo segue o seguinte padrão:
    - código da coligada + número do pedido de exame + Sequencia exame + "." + código do laudo + ".xml"
    - Exemplo: 11490061.xml
  + Ao importar o arquivo xml, o sistema realiza o seguinte processo:
    - Atualiza o pedido de exame indicando o médico responsável;
    - Copia o arquivo para pasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Requisicao\Resposta\Processado;**
  + Conteúdo:

| *<?xml version="1.0" encoding="ISO-8859-1"?> <MWL\_ITEM>   <ACTION>SAVE</ACTION>   <WS\_UID>11490061</WS\_UID>   <SITE>CENTRO CIRÚRGICO</SITE>   <PATIENT\_ID>50194</PATIENT\_ID>   <PATIENT\_NAME>JOAO JOSE</PATIENT\_NAME>   <PATIENT\_BIRTHDATE>19601108</PATIENT\_BIRTHDATE>   <PATIENT\_SEX>M</PATIENT\_SEX>   <PATIENT\_EMAIL\_CONSENT>N</PATIENT\_EMAIL\_CONSENT>   <PATIENT\_LOCATION>Andar: 2 - 236-3</PATIENT\_LOCATION>   <ACCESSION\_NUMBER>11490061</ACCESSION\_NUMBER>   <REFERRING\_PHYSICIAN>Dr Matheus</REFERRING\_PHYSICIAN>   <REFERRING\_PHYSICIAN\_IDENTIFICATION>64004</REFERRING\_PHYSICIAN\_IDENTIFICATION>   <REQUESTING\_DEPARTMENT>CENTRO CIRÚRGICO</REQUESTING\_DEPARTMENT>   <MODALITY>US</MODALITY>   <REQUESTED\_PROCEDURE\_DESCRIPTION>RX - ABDOMEN SIMPLES - A.P. - 40808017</REQUESTED\_PROCEDURE\_DESCRIPTION>   <SCHEDULED\_PERFORMING\_PHYSICIAN>   </SCHEDULED\_PERFORMING\_PHYSICIAN>   <SCHEDULED\_STATION\_AE\_TITLE>   </SCHEDULED\_STATION\_AE\_TITLE>   <SCHEDULED\_PROCEDURE\_STEP\_ID>1</SCHEDULED\_PROCEDURE\_STEP\_ID>   <DATE>20250211</DATE>   <TIME>084913</TIME>   <REQUESTED\_PROCEDURE\_ID>30011</REQUESTED\_PROCEDURE\_ID>   <READING\_PHYSICIAN\_DETAILS>     <CODE>32980</CODE>   </READING\_PHYSICIAN\_DETAILS>    </MWL\_ITEM>* |
| --- |

4) Resposta (Carestream) em PDF (Laudo) de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Relatorio\Resposta;**
  + Nome do arquivo segue o seguinte padrão:
    - código da coligada + número do pedido de exame + Sequencia exame + "." + código do laudo + ".pdf"
    - Exemplo: 11490061.pdf
  + Ao importar o arquivo de laudo, o sistema realiza o seguinte processo:
    - Salva o arquivo na tabela SZARQUIVO;
    - Copia o arquivo para pasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Relatorio\Resposta\Processado;**
    - Exclui o arquivo da pasta **...\Saude\Coligada\_X\Filial\_0\Carestream\Relatorio\Resposta;**

**ESTRUTURA DE PASTAS:**

* A pasta principal esta definida na configuração do host: ;
* A partir da pasta principal, é criado uma subpasta padrão, seguindo as regras por coligada: . Observação: Como o controle de arquivo da integração é única para todas as unidades de atendimento, é criado uma pasta única de filial com o código 0, Exemplo: **...\Saude\Coligada\_X\Filial\_0\Carestream, onde X é o código da coligada**
* Após a pasta padrão, é criado outras subpasta, exemplos:
  + **...\Saude\Coligada\_X\Filial\_0\Carestream\Requisicao\Resposta\Processado**
  + **...\Saude\Coligada\_X\Filial\_0\Carestream\Relatorio\Resposta\Processado**
