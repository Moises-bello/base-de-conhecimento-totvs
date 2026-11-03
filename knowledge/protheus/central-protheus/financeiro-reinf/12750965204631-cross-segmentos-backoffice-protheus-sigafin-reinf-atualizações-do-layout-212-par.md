---
article_id: 12750965204631
category: Financeiro - Reinf
content_hash: 99681ca77d100ae7b2c94fb5aab7ba5a6790368ff635826f7de42f6389fe06b8
fetched_at: '2026-06-28T22:37:51.888214+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - REINF - Atualizações do layout
  2.1.2 para o módulo financeiro
type: support-article
updated_at: '2024-06-28T20:07:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12750965204631-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-REINF-Atualiza%C3%A7%C3%B5es-do-layout-2-1-2-para-o-m%C3%B3dulo-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16444647234199) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**Quais as atualizações necessárias para atender o REINF 2.1.2 para o módulo financeiro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.33   
  
**Solução**A adequação do time **TAF Fiscal** para a entrega da **REINF** versão 2.1.2. foi concluída e publicada no portal do cliente. Com este pacote e o do Backoffice disponibilizado nos links abaixo, será possível realizar as integrações e as apurações dos eventos do **bloco 40** da **EFD-REINF**.  
É imprescindível a aplicação dos pacotes de atualização do **SIGATAF,** **Backoffice** e seus 2 dicionários de dados (**SDFBRA**) para utilização das novas funcionalidades criadas para a **REINF 2.1.2.**  
Recomendamos a aplicação dos pacotes primeiramente em ambiente de homologação para que seja possível realizar os testes com o **parâmetro MV\_TAFAMBR = 2** (**Ambiente de produção restrita da EFD-REINF)** e o **parâmetro MV\_TAFVLRE = 2\_01\_02 (nova versão).**Pacote **TAF**:  
**12.1.33:** [https://suporte.totvs.com/portal/p/10098/download#detail/1044899](https://suporte.totvs.com/portal/p/10098/download#detail/1043538)  
**12.1.2210:** [https://suporte.totvs.com/portal/p/10098/download#detail/1084565](https://suporte.totvs.com/portal/p/10098/download#detail/1084563)  
**12.1.2310:** <https://suporte.totvs.com/portal/p/10098/download#detail/1126399>  
**Menu:** <https://suporte.totvs.com/portal/p/10098/download?e=1096024>

   
Pacote **Backoffice**:  
[Expedição Continua Backoffice Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160#issues-15)  
**12.1.33**: <https://suporte.totvs.com/portal/p/10098/download#detail/1039095>  
**12.1.2210**: <https://suporte.totvs.com/portal/p/10098/download#detail/1080333>  
**12.1.2310:** <https://suporte.totvs.com/portal/p/10098/download#detail/1123867>  
   
Para a transmissão dos eventos no novo layout, será necessário aplicar o pacote da expedição contínua e atualização dos Schemas do **TSS**.  
Pacote **TSS (Aplicar no RPO do TSS):**  
**12.1.33**: <https://suporte.totvs.com/portal/p/10098/download?e=1043352>  
**12.1.2210**: <https://suporte.totvs.com/portal/p/10098/download?e=1080454>  
**12.1.2310:** <https://suporte.totvs.com/portal/p/10098/download?e=1080454#detail/1124963>  
[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

```
Observação: Para a versão 12.1.33 é necessário ter a garantia estendida.
```

**Saiba mais**  
[TAF - EFD-Reinf](https://tdn.totvs.com/display/TAF/EFD-Reinf)  
[EFD-REINF](https://tdn.totvs.com/display/public/PROT/EFD-REINF)
