---
article_id: 360038473854
category: GPE - eSocial - Periódicos
content_hash: 7b26cf4b93463a0bcd2649f3a849fb07caf69e32803ddfc1cbb56782d7637d3e
fetched_at: '2026-06-28T22:45:07.286298+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - No evento S-1200 o sistema está
  trazendo valores de dissidio que já foi pago em folhas (S-1200) de meses anteriores
type: support-article
updated_at: '2025-07-22T12:18:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038473854-RH-Linha-Protheus-GPE-eSocial-S-1200-No-evento-S-1200-o-sistema-est%C3%A1-trazendo-valores-de-dissidio-que-j%C3%A1-foi-pago-em-folhas-S-1200-de-meses-anteriores
---

**Ocorrência**No evento S-1200 o sistema está trazendo valores de dissidio que já foi pago em folhas (S-1200) de meses anteriores.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões **Causa**O erro acontece devido ao código da verba de Folha Mensal estar preenchido no campo **Verba de Dissidio (RV\_CODCOM\_)** onde deve ser preenchido apenas código de verba que é utilizado para pagar diferença de dissidio. e não verbas que são utilizadas no calculo da folha mensal.

**Solução**  
As verbas que são utilizadas na folha de pagamento mensal não devem ser preenchida no campo **Verba de Dissidio (RV\_CODCOM\_)** do **cadastro de verbas (SRV)** do **GPE.** Acesse Atualizações - definição calculo - verbas - aba dissidio:

**Por Exemplo:**A verba de **ID 0112 (Salario Mensal)** e **ID 0148 (INSS Empresa)** são verbas utilizadas no calculo da folha mensal, e por isso a diferença do dissidio não pode ser paga nessa verba. No campo **Verba de Dissidio (RV\_CODCOM\_)** só deve ser informada verbas especificas para a geração da **Dif. de Dissidio**.   
  
Para conhecer mais sobre IDs do Dissidio e Configuração acesse o link: **[Manual do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-MP-GPE-Manual-do-diss%C3%ADdio-retroativo-?source=search)**  
Nessa situação para analisar se a configuração das verbas está correta acesse sua rotina de cadastro de verbas do GPE e faça um **Filtro** do campo da **Verba de Dissidio**, informando todas as verbas que estão no calculo da folha de um trabalhador com o erro.   
  
Conforme imagens de exemplo abaixo, se voltar algum resultado é essa informação que deverá ajustar. **1.** Clicar em Filtro no cadastro de verbas. **![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050448314)​**

**2.** Clicar em Criar Filtro.

**![](https://totvssuporte.zendesk.com/attachments/token/I6NMLOgLfNvrzN7ulBxUxiECh/?name=inline-2054277905.png)​  
  
3.** Alterar campo conforme imagem abaixo, e no campo expressão colocar o código da verba que está no calculo da folha mensal e não é de dissidio e depois clicar em adicionar.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051355253)**  
Após adicionar para colocar mais verbas clique no botão "OU" e repita o processo acima. E quando finalizar do o filtro clique em salvar.  
 **![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050449374)  
  
4.** Selecione o Filtro criado e clique em aplicar filtro. **​  
![](https://totvssuporte.zendesk.com/attachments/token/WZ2ewKSZXzYYisqpDI02htyaQ/?name=inline317991375.png)​**

No exemplo acima a Verba **101** **- Salario** estava informada no campo **Verba de Dissidio (RV\_CODCOM\_)** da verba **105 - Hora Extra 50%**, desta forma a verba **105 - Hora Extra 50%** está com a configuração incorreta, já que a verba **101** só pode ser utilizada para pagamento de folha mensal e não para pagamento de **Diferença de Dissidio**.  
  
Para corrigir o erro do cenário acima deve deixar vazio o campo Verba de Dissidio (RV\_CODCOM\_) da verba **105 - Hora Extra 50%** e gerar novamente o evento **S-1200** através do GPE.  
  
É importante observar que no campo **Verba de Dissidio (RV\_CODCOM\_) só podem ser informadas verbas específicas para pagamento de diferença de dissidio**.  
  
Para mais informação relacionadas a configuração do Reajuste Retroativo/Dissídio no módulo **GPE**acesse a página do **[MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)**.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
