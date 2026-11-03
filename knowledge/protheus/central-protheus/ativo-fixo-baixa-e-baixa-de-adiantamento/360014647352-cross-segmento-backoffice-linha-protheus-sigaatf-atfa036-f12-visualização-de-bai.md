---
article_id: 360014647352
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 4cd2e6dd1dc614b9107e03fee4fd0ca47dba42f47d730b271e6877fa50676834
fetched_at: '2026-06-28T22:41:55.547774+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036- F12:  Visualização
  de Baixas '
type: support-article
updated_at: '2022-08-05T18:15:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014647352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-F12-Visualiza%C3%A7%C3%A3o-de-Baixas
---

**Dúvida**Como identificar as legendas e a **visualização** das baixas na rotina **ATFA036**?

**Ambiente**Microsiga Protheus - Ativo Fixo - a partir da versão 12  
  
**Solução**A **visualização** das baixas do **ativo fixo** pode ser realizada de 3 formas.  
Modo de visualização da Browser da rotina de baixa de Ativos:

Acionar a tela com a tecla F12

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970426874135/mceclip0.png)

Detalhes sobre as opções de visualização abaixo:

1 - Baixas de Ativo: Serão exibidos os registros de baixas de ativos já efetuadas.

Definição feita com base na Tabela FN6

FN6\_STATUS == 1 **Verde** (Baixa Ativa)

FN6\_STATUS == 2 **Vermelho** (Baixa Cancelada)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970534294679/mceclip1.png)

2 - Tipos de Ativo: Serão exibidos os registros dos tipos de ativo das fichas cadastradas no ambiente Ativo Fixo, baixados e/ou com saldo disponível.

Definição feita com Base na Tabela SN3 e FN7

N3\_BAIXA == 0 **Verde** (Ativo fixo Vigente)

N3\_BAIXA >0 e N3\_DTBAIXA = preenchido **Vermelho** (Ativo Fixo Baixado)

Se houve transferência **Rosa** (Ativo Transferido de Filial)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970573164183/mceclip2.png)

3 - Ativos: Serão exibidos os registros dos ativos cadastrados no ambiente Ativo Fixo, baixados, disponíveis e/ou transferidos de filial.

Se não foi totalmente baixado e N1\_STATUS diferente de 4 **Verde** (Ativo Disponível)

Se não tiver em branco N1\_BAIXA e N1\_STATUS diferente de 4 **Vermelho** (Ativo Baixado)

Se N1\_STATUS = 4 **Rosa** (Ativo Transferido de filial)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970680125079/mceclip3.png)
