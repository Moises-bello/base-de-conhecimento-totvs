---
article_id: 360019758691
category: Gestão de Transportes (TMS)
content_hash: 504b45dda5e828f58804d68a17599bc83f81655dd8005f6adcf6fea77891d637
fetched_at: '2026-06-28T22:45:27.571848+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Configurações referente ao horário de verão
  quando o parâmetro MV_HORARMT está igual a 3 - Fuso horário da filial corrente
type: support-article
updated_at: '2021-08-27T12:06:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019758691-Log%C3%ADstica-Linha-Protheus-TMS-Configura%C3%A7%C3%B5es-referente-ao-hor%C3%A1rio-de-ver%C3%A3o-quando-o-par%C3%A2metro-MV-HORARMT-est%C3%A1-igual-a-3-Fuso-hor%C3%A1rio-da-filial-corrente
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:50 min  
  
Dúvida**Como realizar as configurações referente ao horário de verão quando o parâmetro **MV\_HORARMT** está igual a **3 - Fuso horário da filial corrente**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para ocorrências em relação ao horário de verão onde a filial fica em uma região onde não contempla o horário de verão, porém os documentos são emitidos por uma unidade que possui tratativa de horário de verão, é necessário configurar o Sistema da seguinte forma:

1. Todos os parâmetros listados abaixo devem estar cadastrados no **Configurador** compartilhados, ou seja, sem filial informada:
   * **MV\_HVERAO**: preencher com **.T.** se o servidor estiver em estado com horário de verão;
   * **MV\_HORARMT**: **3 - fuso horário da filial;**
   * **MV\_HVERAOI**: 20181104 - Dia de inicio do horário de verão;
   * **MV\_HVERAOF**: 20190216- Dia de término do horário de verão;
   * **MV\_TMSHRVR**: .T. - habilita o horário de verão para o **TMS - Transportation Management Systems;**
   * **MV\_TMSHRFL**: preencher com o código das filiais que não aderiram o horário de verão. Exemplo - D BA 01 / D BA 02 /. Caso a empresa possua somente uma filial, será necessário colocar o código da mesma com o espaço e a barra: D BA 01 /.
2. Incluir o parâmetro abaixo como exclusivo, ou seja, com filial informada:
   * **MV\_ESTADO**: deve estar configurado com o estado da filial - deve ser exclusivo por filial.

Após as parametrizações no configurador, acessar no módulo do **TMS**a opção **Miscelânea** / **Cte Sefaz**. Dentro da rotina, clicar na opção **Outras** **Ações**/ **Parâmetros**/ **Eventos**e ajustar os parâmetros conforme sua região. Segue abaixo exemplo de como proceder:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014335432/mceclip1.png)

Este processo pode ser efetuado também por meio da opção **Atualizações**/ **Recebimento**/ **Entrada** **Documentos** **Clientes**e dentro da rotina clicar em **Outras** **Ações**/ **Cálculo** **de** **Frete**/ **CTE**/ **Parâmetros**/ **Eventos**.

Para o **MDF-e** é necessário também acessar no módulo do **TMS**a opção **Atualizações**/ **Viagens modelo 2** e dentro da rotina clicar em **Outras** **Ações**/ **Manutenção**/ **Manifesto /** **MDF-E**- **Parâmetros**e ajustar os parâmetros conforme sua região. Segue abaixo exemplo de como proceder:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014339331/mceclip5.png)

No arquivo **appserver.ini**, disponível dentro da estrutura de pastas do **TSS - TOTVS Sped Service**, a chave **SPED\_HVERAO**. Esta chave define se o local em que o servidor do **TSS** se encontra instalado está em horário de verão.  
  
Os conteúdos válidos são**1 - Sim** ou **2 - Não**.  
  
Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014338091/mceclip2.png)

Após efetuar todas as parametrizações citadas acima, é necessário retransmitir o documento, caso esteja com alguma rejeição atrelada ao horário de verão.
