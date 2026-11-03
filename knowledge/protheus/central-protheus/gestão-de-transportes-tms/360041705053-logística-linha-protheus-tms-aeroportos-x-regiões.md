---
article_id: 360041705053
category: Gestão de Transportes (TMS)
content_hash: 16fe824803543b8ee39e7956afff3ed5f2dc92ac93226c5bc828f5866859058f
fetched_at: '2026-06-28T22:45:27.219066+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Aeroportos x Regiões
type: support-article
updated_at: '2023-08-28T11:16:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041705053-Log%C3%ADstica-Linha-Protheus-TMS-Aeroportos-x-Regi%C3%B5es
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17080945009175)*** Tempo aproximado para leitura: **00:05:00 min****Dúvida**Qual a finalidade e como utilizar a **Rotina Aeroportos x Regiões**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**A rotina **Aeroportos x Regiões** - **TMSA910** tem como finalidade vincular as regiões cadastradas aos Aeroportos de uso para geração do **AWB** **-** **Air Waybill** ou **Conhecimento de Transporte Aéreo**.  
  
As Regiões em questão são as geradas na rotina **Estrutura de Regiões -** **TMSA120** bem como os Aeroportos fazem parte da tabela padrão **M9** da **SX5**.  
  
Para o devido uso:

* Acesse a rotina em **Atualizações/Viagens/Áereo Transporte/Aeroportos x Regiões - TMSA910**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055709893)

* Na tela inicial, é apresentado um *grid* contendo todos os itens já cadastrados e os botões dispostos para inteiração;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054832614)

* Para um novo registro, clicamos em **incluir**;
* Na tela a seguir, informamos a região de cálculo que será usado para a geração do **AWB**;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055710033)

* No *grid* abaixo, serão informados todos os aeroportos, campo **DD7\_CODAER** e tempo de translado, campo **DD7\_TMPTRA** do local de origem até o mesmo;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055710393)

* Após confirmado os dados, clicar em **Salvar**.

**Saiba mais**Para entender melhor o funcionamento do processo de geração de **AWB**, segue documentações de apoio:

1. **[Geração AWB;](https://tdn.totvs.com/pages/releaseview.action?pageId=526996671)**
2. **[Gera Fatura AWB;](https://tdn.totvs.com/pages/releaseview.action?pageId=527002025)**
3. **[Grades de Voo;](https://tdn.totvs.com/pages/releaseview.action?pageId=526994219)**
4. **[Libera Fatura AWB.](https://tdn.totvs.com/pages/releaseview.action?pageId=526996345)**
