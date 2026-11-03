---
article_id: 360016697191
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 81d753183f0ccdc75436ad2d5f1894ca26857f8cdf3dbb56a2d6696cc519c811
fetched_at: '2026-06-28T22:37:56.206522+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 Como gerar
  despesa bancária no retorno do CNAB
type: support-article
updated_at: '2024-07-17T20:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016697191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-Como-gerar-despesa-banc%C3%A1ria-no-retorno-do-CNAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24972208911383)**Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como gerar despesa bancária no retorno do CNAB?

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975727873431)](https://centraldeatendimento.totvs.com/hc/article_attachments/24975727873431)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

A despesa de cobrança ocorre quando seu layout de retorno possui preenchimento da linha **Despesa de cobranças = Vlr Desp Cobr**.  Acesse o módulo **Financeiro**, **Atualizações**, **Cadastro** , **Parâmetros** **Bancos** e selecione o cadastro de um determinado banco e verifique o preenchimento do campo: **Desp. Princ (EE\_DESPCRD) .** A forma que este campo será preenchido, é a forma que será calculado e gerado a despesa de cobrança no Retorno **(FINA200):**

Para não gerar a despesa de cobrança, deixe o campo **(posição)** em branco na linha: **Despesa de cobranças = Vlr Desp Cobr** no seu layout de retorno para que o sistema não calcule o valor de despesas.

### **Configuração de modelo 1 e modelo 2 na despesa de cobrança.**

**- Modelo 1 ->** Definir apenas a faixa de posição referente a despesa bancária no layout de retorno do banco.

**- Modelo 2 ->** Definir a faixa de posição referente a despesa bancária no layout de retorno do banco e definir o conteúdo dessa faixa de posição com a variável **DESPESA.**

**Exemplo: Dentro do arquivo de retorno do banco**

Essas configurações dentro do arquivo de retorno, são para não apresente na coluna consistência os status "Valor Maior" ou "Valor Menor" ao emitir o relatório "FINR650 - Relatório de Retorno CNAB"

Editando um arquivo de retorno do banco ITAU.RET , e confrontando as posição do layout com o campo EE\_DESPCRD **[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975423051799)](https://centraldeatendimento.totvs.com/hc/article_attachments/24975423051799)**

**Exemplo: Emissão do relatório de retorno CNAB**

FINR650 - Relatório de Retorno CNAB com **EE\_DESPCRD = N**

Onde no Valor Recebido está com o conteúdo **R$ 100,00**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391411095)](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391411095)

**Exemplo: Emissão do relatório de retorno CNAB**

FINR650 - Relatório de Retorno CNAB com **EE\_DESPCRD = S**

Onde no "Valor Recebido" dentro do arquivo de retorno do banco está com o conteúdo **R$ 98,00** (Porém no relatório ficará R$ 100,00 no valor recebido)

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391413783)**](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391413783)

**Exemplo de baixa CNAB**

Como ficaria a "FINA100 - Movimentação Bancária" após a baixa do CNAB com **EE\_DESPCRD = N**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975423064983)**](https://centraldeatendimento.totvs.com/hc/article_attachments/24975423064983)

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391428887)**](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391428887)

**Exemplo de baixa CNAB**

Como ficaria a "FINA100 - Movimentação Bancária" após a baixa do CNAB com **EE\_DESPCRD = S**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391432087)**](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391432087)

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391437207)**](https://centraldeatendimento.totvs.com/hc/article_attachments/24975391437207)

**Em ambos os cenários:**

Será realizado uma movimentação bancária a receber no valor de R$ 100,00 referente ao valor do título.

E outra movimentação bancária a pagar no valor de R$ 2,00 referente a despesa (ex: Taxa impressão de Boleto)

Essa movimentação de despesa é parecido com uma inclusão de movimentação a pagar realizada pela rotina "FINA100 - Movimentação Bancária", mas o título e a taxa não tem amarrações, são independentes.

**Importante**: Caso necessário efetuar um **estorno da despesa,** terá que acessar a rotina "FINA100 - Movimentação Bancária" e efetuar uma movimentação contrária referente ao valor da despesa, e informar no histórico, já que o estorno da baixa do título, não estorna a despesa que foi gerada automaticamente via CNAB, pois , são independentes.

Ponto de entrada **F200VAR**possibilita manipular as informações (variáveis) no retorno do CNAB a Receber (**FINA200**).   
[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=235308494)

**Parâmetros:**

**MV\_NATDPBC -** responsável por definir a natureza da despesa bancária.

**MV\_BXCNAB -** se estiver com conteúdo **'S'** o sistema gera um registro na **SE5** referente a soma de todas as despesas e com conteúdo **'N'** o sistema gera um registro de despesa para cada registro.

**Importante**

Validação e configuração de CNAB não faz parte do nosso escopo de atendimento Help Desk, esse tipo de procedimento se faz necessário analista especialista CNAB, caso não tenha conhecimento, entre em contato com seu executivo de soluções Totvs (ESN).

**Saiba mais**

**[Comunicação Bancária](http://tdn.totvs.com/pages/releaseview.action?pageId=240288856)**
