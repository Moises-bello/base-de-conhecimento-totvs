---
article_id: 360049612273
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 2d0ec33464fa8cb84fa6bdcaa05c6424dc3eb02463ece0327d96cebccedbc207
fetched_at: '2026-06-28T22:40:44.714724+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD Registro 0020 Descentralizada
  no registro 0000 (IND_CENTRALIZADA).
type: support-article
updated_at: '2022-06-10T13:17:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049612273-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Registro-0020-Descentralizada-no-registro-0000-IND-CENTRALIZADA
---

**Dúvida**

0020 Erro : Registro obrigatório não encontrado. Houve indicação de modalidade de escrituração descentralizada no registro 0000 (IND\_CENTRALIZADA).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074065053/mceclip1.png)  
   
 **Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80

**Causa**

* Foi liberado pela receita  no registro 0000 o campo IND\_CENTRALIZADA, onde ao ser preenchido "1 =Escrituração Descentralizada" necessário que o registro 0020 também seja gerado

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072870354/mceclip2.png)

* Ao clicar no erro o sistema direciona para a tela Registro 0020 que não foi gerado

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072873474/mceclip10.png)

* Ao informar parâmetro abaixo "Sem Centralização"

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074065593/mceclip3.png)

* Selecionado somente uma filial (somente um CNPJ)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074065773/mceclip4.png)

O sistema gera o campo " IND\_CENTRALIZADA =1" porem o registro 0020 não é gerado

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072871254/mceclip5.png)

**Solução**

* O manual da receita descreve ao preencher o parâmetro " IND\_CENTRALIZADA =1" necessário que seja gerado registro 0020 , quando existir mais de uma CNPJ na geração do arquivo

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072871374/mceclip6.png)

* gerando uma ECD descentralizada (Registro 0000 campo 21 IND\_CENTRALIZADA =1)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074065593/mceclip3.png)

* O  [ECD Registro 0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024400351-MP-SIGACTB-ECD-Registro-0020-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Descentralizada?source=search)  só será gerado no arquivo ao selecionar mais de um Filial (CNPJ diferentes)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072872074/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074067373/mceclip9.png)

Posição consultoria Tributária

<https://tdn.totvs.com/pages/viewpage.action?pageId=270081687>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074070573/mceclip0.png)

**Conclusão**

para que o 0020 seja gerado e o dados (cadastros e saldos) também seja gerado correto o contado deve verificar junto a receita se vai gerar a ECD [centralização e descentralizada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125892-MP-SIGACTB-ECF-e-ECD-Centraliza%C3%A7%C3%A3o-e-descentralizada?source=search)
