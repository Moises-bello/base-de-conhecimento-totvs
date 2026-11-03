---
article_id: 360018522692
category: RH - Contabilização
content_hash: 548adf3d168297babbfed416eece3644551ece35a1e5392dd63984239e1fb967
fetched_at: '2026-06-28T22:43:45.825924+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como contabilizar valores negativos de provisão
type: support-article
updated_at: '2025-07-29T13:58:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018522692-RH-Linha-Protheus-GPE-Como-contabilizar-valores-negativos-de-provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33791394971927)** Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como deve ser feita a tratativa para contabilizar valores negativos de provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução:**Os valores negativos de provisão apresentados na SRZ, não são contabilizados.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014285092)  
  
 **A) Passo 1:**No cadastro de lançamento padrão, parametrizar os campos de contas débito e crédito com fórmulas que façam o tratamento de inversão das contas quando o valor for negativo (débito para crédito / crédito para débito).  
  
Exemplo:

Conta Débito:  IIF(SRZ->RZ\_VAL<0,"001","002")    
Conta Crédito: IIF(SRZ->RZ\_VAL<0,"002","001")    
  
**- Acesse: Atualizações > Cadastros > Lançamento Padrão**  
![KCS__PATRICIA_06.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360014286051)  
  
  
Também no lançamento padrão deve ser tratado com fórmula, o campo **Vlr Moeda 1**, utilizando a função ABS, esta função retornará um número não negativo. <http://tdn.totvs.com/display/tec/Abs>).   
  
Exemplo:  
  
VLR MOEDA 1: ABS(SRZ->RZ\_VAL)

![KCS__PATRICIA_07.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360014286771)

**B) Passo 2:**Após configuração do lançamento padrão, acessar a rotina através do Menu: **Miscelanea-> Fechamentos -> Contabilização**e processar a contabilização.  
Os lançamentos na contabilização já estarão tratados, de modo que serão apresentados sem os valores negativos.   
  
![KCS__PATRICIA_09.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360014288891)

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
