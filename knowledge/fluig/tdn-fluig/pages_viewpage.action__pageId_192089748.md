---
content_hash: 4269989e334f5c8034a5dc9e55711e0ec1b7a2468721627adc2c675953725386
fetched_at: '2026-06-28T21:35:19.123151+00:00'
page_id: '192089748'
product: fluig
source: tdn-fluig
title: Migração de palavras chave do ECM para a plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=192089748
version: 9
---

# Índice

# Objetivo

---

O objetivo deste guia é indicar um método de migração das palavras chave dos documentos de uma base do **TOTVS | ECM** para uma base convertida para o **TOTVS Fluig Plataforma**. Estas palavras chave serão inseridas no Fluig como 'Comentário adicional' no documento.

# Procedimento de Migração e Conversão de Dados

---

Atenção

Esta operação deve ocorrer depois da conversão de uma base **TOTVS | ECM** para a plataforma. Uma cópia da base do **TOTVS |** **ECM** antes da conversão deve ser mantida como *backup.*

Acompanhe a seguir o check-list para a migração das palavras chave do **TOTVS | ECM**.

1. Possuir uma cópia da base do **TOTVS | ECM**antes da conversão para o **Fluig**.
2. Ter realizado a conversão de acordo com esta documentação: [Conversão TOTVS ECM para a plataforma TOTVS Fluig](http://tdn.totvs.com/x/qANbDw).
3. Realizar uma cópia da base convertida para realizar testes na base antes de realizar a migração das palavras chave*.*

# Utilização do Aplicativo de conversão

---

false11Passo 1Passo 1

**Passo 1: Download do aplicativo que realizará a conversão**

Se você ainda não possui o aplicativo que realiza a conversão faça o download aqui:

2Passo 2

**Passo 2: Execução do aplicativo**

Após o download do aplicativo, extraia seu conteúdo para uma pasta e execute o arquivo: **ConvertKeywordsEcmToFluig.jar.**

3Passo 3

**Passo 3: Dados das bases de dados**

No aplicativo é necessário inserir os dados da base do **TOTVS | ECM** e da base convertida do**Fluig,** de preferência realizar a conversão com as bases de cópia para evitar acidentes, conforme o exemplo na imagem a seguir:

4Passo 4

**Passo 4: Execução da Conversão**

Após a inserção dos dados das bases de dados, o programa avisará que este processo pode levar alguns minutos, dependendo do tamanho de sua base, só feche o programa após a notificação no log de que a conversão foi executada com sucesso. Caso ocorra algum erro ao conectar em alguma das bases de dados o aplicativo irá notificar.

Após a conversão realizada com sucesso o *log* ficará como a imagem a seguir:
