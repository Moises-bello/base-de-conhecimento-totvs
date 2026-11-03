---
article_id: 4407246050839
category: Gestão de Distribuição (SIGAOMS)
content_hash: 138f62d38ac833abefdc7af1b6f793e63a19f2e37211e6beb938f0675c04cd0e
fetched_at: '2026-06-28T22:45:51.020224+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Sequência de Numeração das Notas Fiscais
  no Faturamento por Carga MATA460B-OMSA460B
type: support-article
updated_at: '2022-12-01T11:08:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407246050839-Log%C3%ADstica-Linha-Protheus-OMS-Sequ%C3%AAncia-de-Numera%C3%A7%C3%A3o-das-Notas-Fiscais-no-Faturamento-por-Carga-MATA460B-OMSA460B
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:48 min** **Dúvida**Como tratar a **Sequência de Numeração das Notas Fiscais** no Faturamento por Carga **MATA460B-OMSA460B** no **TOTVS OMS**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12.  
  
**Solução**No **TOTVS OMS - Order Management System**, temos o parâmetro **MV\_OMSSMNF,** que tem a função de controlar o sequenciamento da **Numeração de Notas Fiscais por Carga e Usuário**. Pode ser parametrizado como **.T. - Verdadeiro** ou **.F.** **- Falso.**O parâmetro **MV\_OMSSMNF**, poderá ser utilizado, quando existirem mais de um usuário realizando o **Faturamento de Carga - MATA460B-OMSA460B**, onde o Sistema não segue uma ordem na geração da **Numeração das Notas Fiscais x Carga**. Exemplo:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407260510487/mceclip10.png)

A imagem acima demonstra que de acordo com a performance do ambiente, as Notas Fiscais são geradas **entre as Cargas**. Com o parâmetro **MV\_OMSSMNF** ativo, o processo seguirá da seguinte forma:  
  
**O usuário 1 está Faturando:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407269368343/mceclip6.png)

Ao abrir a tela para selecionar a **Série/Notas**, o usuário irá bloquear o faturamento, pois está selecionando a **numeração/sequenciamento das Notas Fiscais**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407259847319/mceclip7.png)

O **usuário 2** permanece com a permissão de acesso na tela:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407260693271/mceclip12.png)

Ao clicar em **Prep. Doc** será exibida a mensagem abaixo:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407274004119/mceclip9.png)

A mensagem é exibida ao **constatar um faturamento**. O tempo de uma nova tentativa sem a interação com o usuário é de **3 segundos**. Caso o usuário clicar em **Confirmar**, será realizada uma nova tentativa de faturamento.  
 **Resultado esperado:**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407260520343/mceclip11.png)

**Saiba mais**  
Mais informações poderão ser acessadas no *link*: [Sequência de Numeração das NFs no Faturamento por Carga - MATA460B - OMSA460B](https://tdn.totvs.com/pages/releaseview.action?pageId=635351695)
