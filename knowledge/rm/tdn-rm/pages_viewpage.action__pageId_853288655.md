---
content_hash: 7c09facf62f840f8d244b5fbebb097eedf1d9c1cdb5490e0eeb5514c9259ae1b
fetched_at: '2026-06-29T00:11:54.104859+00:00'
page_id: '853288655'
product: rm
source: tdn-rm
title: Importação das tabelas do SUS (ImportaSus)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853288655
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Funcionalidade que realiza a importação das tabelas do SUS, disponibilizadas mensalmente.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Importante!

O arquivo ZIP do ImportaSUS deve ser baixado através da nossa central de downloads da TOTVS.

Para que seja possível executar a rotina do Importa Sus, é  necessário realizar os seguintes passos:

1. Acessar o menu Ambiente | Processos | Segurança de Jobs fracionáveis
2. Incluir a classe do job SauImportaSusSliceableProcess para os perfis que possuem acesso
3. O ambiente deve estar configurado para utilizar 3 camadas
4. Habilitar o processamento de jobs e configurar a quantidade de execuções simultâneas (este número é que possibilitará a execução mais rápida da importação)

Acesse o menu Faturamento | Outros | Atualização de Preços | Importa Sus

Importante!

Agora, não é mais necessário descompactá-lo antes de iniciar o processamento

Selecione o arquivos zip, contendo as tabelas da competência desejada.

Caso seja necessário atualizar a tabela de CEPs utilizada no SUS, marque a opção.

Clique em **Avançar** e depois clique em **Confirmar**

Um agendamento da execução do processo será feita e o mesmo será executado em breve.

Clique no botão "Acompanhar processo", para acessar a tela com a execução do mesmo

O processo criado já vem filtrado nessa tela.

Neste momento ainda não será possível acompanhar o progresso da execução. Será necessário clicar nos 3 pontinhos e quando o processo for finalizado, o opção de "Visualizar log" será habilitado

Ao término, serão exibidas as mensagens.

Caso queira visualizar o log completo, clique no botão de Visualizar log.

Note que serão criados 6 processo . O primeiro é o processo principal que controlará os outros 5. Portanto serão criados 5 processos para realizar a importação de todas as tabelas disponibilizadas, assim garantimos uma execução mais rápida.

Tabelas utilizadas

## **03.** **TABELAS UTILIZADAS**

* ```
  SZHISTORICOIMPORTASUS
  ```
* ```
  SZSUSTUCID
  ```
* ```
  SZSUSEQUIPECNES
  ```
* ```
  SZSUSTUDETALHE
  ```
* ```
  SZSUSTUFINANCIAMENTO
  ```
* ```
  SZSUSTUFORMAORGANIZACAO
  ```
* ```
  SZSUSTUGRUPO
  ```
* ```
  SZSUSTUGRUPOHABILITACAO
  ```
* ```
  SZSUSTUHABILITACAO
  ```
* ```
  SZSUSTUMODALIDADE
  ```
* ```
  SZSUSTUOCUPACAO
  ```
* ```
  SZSUSTUPROC
  ```
* ```
  SZSUSTUREGISTRO
  ```
* ```
  SZSUSTURUBRICA
  ```
* ```
  SZSUSTUSERVICO
  ```
* ```
  SZSUSTUSERVICOCLASSIFICACAO
  ```
* ```
  SZSUSPROCDETALHE
  ```
* ```
  SZSUSTUSIASIH
  ```
* ```
  SZSUSTUSUBGRUPO
  ```
* ```
  SZSUSTUTIPOLEITO
  ```
* ```
  SZSUSTUEXCCOMPATIBILIDADE
  ```
* ```
  SZSUSTUPROCCID
  ```
* ```
  SZSUSTUPROCCOMPATIVEL
  ```
* ```
  SZSUSTUPROCDETALHE
  ```
* ```
  SZSUSTUPROCHABILITACAO
  ```
* ```
  SZSUSTUPROCINCREMENTO
  ```
* ```
  SZSUSTUPROCLEITO
  ```
* ```
  SZSUSCEPMUNICIPIO
  ```
* ```
  SZSUSTUPROCORIGEM
  ```
* ```
  SZSUSTUPROCREGISTRO
  ```
* ```
  SZSUSTUPROCSERVICO
  ```
* ```
  SZSUSTUPROCSIASIH
  ```
* ```
  SZNACIONALIDADE
  ```
* ```
  SZSUSIBGE
  ```
* ```
  SZSUSDETALHE
  ```
* ```
  SZSUSCLINICA
  ```
* ```
  SZSUSPROCESPECIALIDADE
  ```
* ```
  SZSUSTUPROCMODALIDADE
  ```
* ```
  SZSUSCNAE
  ```
* ```
  SZSUSCARACINTERN
  ```
* ```
  SZSUSMOTCOBR
  ```
* ```
  SZSUSDETALHECOBR
  ```
* ```
  SZSUSCHECKLISTHOSP
  ```
* ```
  SZSUSPROCDETALHEHOSP
  ```
* ```
  SZSUSPROCDETALHECOBR
  ```
* ```
  SZSUSTUPROCOCUPACAO
  ```

```

```
