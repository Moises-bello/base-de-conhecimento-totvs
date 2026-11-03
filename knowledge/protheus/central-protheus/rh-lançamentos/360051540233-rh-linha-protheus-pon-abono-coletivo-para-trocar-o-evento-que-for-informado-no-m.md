---
article_id: 360051540233
category: RH - Lançamentos
content_hash: 75b31fbc1e6d0c945911774d02300f000a242532b20426b97efdcb5b23aba336
fetched_at: '2026-06-28T22:44:46.737233+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON -  Abono coletivo para “trocar” o evento que for
  informado no motivo de abono (um evento que estava configurado pra ir para folha,
  após o abono coletivo ir para o banco de horas)
type: support-article
updated_at: '2025-06-12T20:48:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051540233-RH-Linha-Protheus-PON-Abono-coletivo-para-trocar-o-evento-que-for-informado-no-motivo-de-abono-um-evento-que-estava-configurado-pra-ir-para-folha-ap%C3%B3s-o-abono-coletivo-ir-para-o-banco-de-horas
---

**Dúvida**Abono coletivo para “trocar” o evento que for informado no motivo de abono. Um evento que estava configurado pra ir para folha, após o abono coletivo ir para o banco de horas. No exemplo foi utilizado um evento de falta, porém, o procedimento pode ser feito para outros eventos.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Cadastre os parâmetros **MV\_ABOSEVE** e **MV\_SUBABAP** com o conteúdo **S**;  
  
2. Na rotina Motivo de Abono, cadastre o campo **Abona Horas** como **NÃO** e no campo **Cód. Evento** informar um evento válido que esteja configurado para banco de horas;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078342514)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078342694)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078699974)

3. Para executar o abono coletivo verifique o apontamento em especifico que deseja abonar, neste caso, o evento 010  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32779723610263)

4. Em Miscelâneas > Cálculos > Abono Coletivo > informe os parâmetros conforme sua demanda  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32779723613335)

Informe o apontamento que deve abonado na pergunta **Eventos Abonados**.   
Na pergunta **Tipo de Abono?** é possível escolher se o abono será **integral** ou **parcial**, caso opte por **parcial**, a pergunta **Horas Abono Parcial?** deve conter a quantidade de horas necessárias.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32779723617815)

 5. Na próxima tela, serão mostradas as matrículas que tiveram este apontamento gerado.  
No campo **Motivo Abono** deve ser lançado o código do abono.![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32779767070999)

6. Após executar o cálculo mensal, o sistema gerou o apontamento de desconto nos Lançamentos de Banco de Horas do funcionário:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079500013)  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
