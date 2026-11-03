---
article_id: 4421889801367
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 3fdb66262959814ad82fafbca9e4bfb98a16cabff374fddad42dcf26a7da6e4c
fetched_at: '2026-06-28T22:40:32.613152+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - TOTVS Backoffice - Linha Protheus - SIGACTB - Contabilização
  com compartilhamento diferente entre módulos 'X'  x SIGACTB
type: support-article
updated_at: '2022-05-16T12:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421889801367-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-compartilhamento-diferente-entre-m%C3%B3dulos-X-x-SIGACTB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:03:00 min** **Dúvida**Quando possuo um compartilhamento diferente entre outros módulos do Protheus (Ativo Fixo, Compras, Estoque, Faturamento, Financeiro e RH) vs Contabilidade Gerencial (SIGACTB), como proceder para que a contabilização dos módulos sejam na filial correta dentro da Contabilidade Gerencial?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - Versão 12.  
  
**Solução**Para esses casos, será necessário utilizar os Pontos de Entrada **ANTCTBGRV** e **DEPCTBGRV**, que foram criados para corrigir a filial de contabilização.  
  
**ANTCTBGRV -** <https://tdn.totvs.com/display/public/PROT/ANTCTBGRV+-+Altera+a+filial+para+gravacao+dos+saldos+e+lancamentos+contabeis.++--+109629>

Exemplo de utilização:

```
#INCLUDE "Protheus.ch"  
  
user function ANTCTBGRV()  
  
Public _cFilSm0Ant := cFilAnt //Guarda a filial posicionada na rotina de origem da contabilização  
cFilAnt := "01" //Altera a filial posicionada, para contabilizar com a filial desejada, no caso a 01  
  
Alert("Passou no PE ANTCTBGRV")  
  
return
```

**DEPCTBGRV -** <https://tdn.totvs.com/pages/releaseview.action?pageId=6068744>

Exemplo de utilização:

```
#INCLUDE "Protheus.ch"  
  
user function DEPCTBGRV()  
  
    cFilAnt := _cFilSm0Ant //Retorna para a filial posicionada antes da contabilização  
  
    Alert("Passou no PE DEPCTBGRV")  
  
return
```

Com isto possibilita manter o compartilhamento diferente entre os módulos 'X' x contabilidade gerencial, e tratar a contabilização para ser executado na filial correta.

É imprescindível realizar as alterações necessárias para que seja gravado as filial conforme a necessidade.

**Informações Relacionadas:**

Pontos de Entrada Contabilidade Gerencial:

- <https://tdn.totvs.com/display/PROT/Pontos+de+Entrada+-+Contabilidade+Gerencial+-+P12>
