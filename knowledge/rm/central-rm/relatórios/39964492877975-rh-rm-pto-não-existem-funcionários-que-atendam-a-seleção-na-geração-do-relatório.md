---
article_id: 39964492877975
category: Relatórios
content_hash: 6d4bc7d7ea35676235999924c5ff33975f5b717866aaf95144a2bf5f08d8bbf5
fetched_at: '2026-06-28T22:46:39.186261+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: RH - RM - PTO - "Não existem funcionários que atendam a seleção" na geração
  do Relatório Espelho do Cartão
type: support-article
updated_at: '2026-04-24T14:10:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39964492877975-RH-RM-PTO-N%C3%A3o-existem-funcion%C3%A1rios-que-atendam-a-sele%C3%A7%C3%A3o-na-gera%C3%A7%C3%A3o-do-Relat%C3%B3rio-Espelho-do-Cart%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39964492867351) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**

Ao tentar gerar o relatório de Espelho do Cartão de Ponto para o funcionário, apresenta a mensagem de aviso  "Não existem funcionários que atendam a seleção", impossibilitando a emissão do relatório.

**Ambiente**

RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões

**Causa**

O incidente ocorre devido à ausência de informações obrigatórias nos históricos do funcionário ou inconsistência nas datas de vigência desses históricos em relação ao período de geração do relatório. O que impede que o relatório seja gerado.

**Solução**

1. No módulo Automação de Ponto, acesse **Cadastros | Funcionários**, selecione a chapa que apresenta o incidente;
2. Acesse em **Anexos** | **Históricos** e verifique os históricos de **Situação**, **Seção,** **Função** e **Utilização do Cartão de Ponto;**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39965316965271)
3. Certifique-se de que existe um registro de histórico válido para o período em que se deseja gerar o espelho do ponto;
4. Caso algum histórico esteja vazio ou com datas divergentes, realize o preenchimento correto das informações;
5. Se o funcionário encontra-se de férias ou afastado em todo período verifique na geração do relatório passo 2 se o parâmetro '**Funcionário de férias/afastado em todo período**' está marcado:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39984623502231)
6. Caso o funcionário não utilize o cartão de ponto, verifique na geração do relatório passo 3 se o parâmetro '**Imprimir funcionários que não utilizam cartão de ponto**' está marcado:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39984645947799)

   7. Após a devida atualização, realize a geração do relatório.

   **Saiba mais**  
   [RH - RM - PTO - Relatório Espelho do Cartão de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9300067656599-RH-RM-PTO-Relat%C3%B3rio-Espelho-do-Cart%C3%A3o-de-Ponto)
