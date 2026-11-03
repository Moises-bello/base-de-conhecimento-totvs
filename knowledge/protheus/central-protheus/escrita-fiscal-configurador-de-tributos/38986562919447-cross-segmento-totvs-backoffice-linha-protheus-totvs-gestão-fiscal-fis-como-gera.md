---
article_id: 38986562919447
category: Escrita Fiscal - Configurador de Tributos
content_hash: ff6a2b6a57d34bdc2357b97acfdb73971e99252dbc656942dda03a0eaa8fd081
fetched_at: '2026-06-28T22:39:17.627184+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS Como gerar cBenef com redução de base de calculo no fisa170?
type: support-article
updated_at: '2026-03-12T13:54:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38986562919447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-gerar-cBenef-com-redu%C3%A7%C3%A3o-de-base-de-calculo-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533564055) Tempo aproximado para leitura: 00:08**min**  
  
**Dúvida**  
Como gerar cBenef com redução de base de calculo no fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Como gerar cBenef de mercadoria com redução de base de calculo no configurador de tributos

Exemplo

mercadoria = 1000,00

redução de base = 51,11%

Base de calculo do ICMS = 488,90\*18% = 88,00

MV\_estado = SP

Cliente = SP

Cadastro de Produtos

Origem = 0

TES

CFOP = 5102

Calculo

ID tributos

ICMS

1a) Cadastro de regra de NCM

8432.90.00

Sp para SP - origem = 0 aliquota de 18%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533564567)

Regra de base de calculo

( O:VAL\_MERCADORIA -  O:DESCONTO +  O:FRETE +  O:SEGURO +  O:DESPESAS ) \* I:PERC\_REDUCAO\_BASE

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533564823)

Regra de aliquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986562898839)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986562899351)

Regra de Escrituração

Incidencia = tributado

Incidencia Parcela Reduzida = outros

CST = 20

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533565975)

Regra de Calculo Documentos Fiscais - ICMS - 000500

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533566359)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533566999)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533567255)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533567639)

Livro Fiscal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533568279)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986562904855)

2a) Regra de Ajuste de lançamento

ICMS diferido = SP020770

Mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986562905751)

O codigo precisa estar na rotina Fisa156

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533569687)

Cadastro Regra de ajuste Lançamento

Tabela 52 - SP020770 - inicio 01/01/2026 - regra tributária = 000500

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533570071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986562909591)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986533571223)

Cbenef

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38986562911767)

Boletim Configurador

https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos
