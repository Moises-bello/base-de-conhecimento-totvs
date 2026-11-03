---
article_id: 10412589165975
category: RH - Contabilização
content_hash: ff46852937b964d6dcb111cb5f7bee25cc5bfac4dfb3b279749ee770ec905db8
fetched_at: '2026-06-28T22:43:45.788823+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir a Contabilização das Provisões quando
  há valores Negativos
type: support-article
updated_at: '2025-07-24T14:11:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10412589165975-RH-Linha-Protheus-GPE-Como-Conferir-a-Contabiliza%C3%A7%C3%A3o-das-Provis%C3%B5es-quando-h%C3%A1-valores-Negativos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33687627170455) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como conferir a Contabilização das Provisões de Férias e 13º Salário quando há valores negativos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Ao realizar a Contabilização das Provisões de Férias e 13º Salário, e realizar as conferências dos valores utilizando os Totais do Relatório de Provisões, quando há valores negativos nas Provisões há diferença entre o valor contabilizado e o valor do relatório de provisão.

Para solucionar essa dúvida, realize os seguintes passos:

1. Verifique se há Tratativa para valores negativos no Lançamento Padrão. Para acessar um modelo de Lançamento Padrão para contabilização dos valores negativos [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018522692-RH-Linha-Protheus-GPE-Como-contabilizar-valores-negativos-de-provis%C3%A3o) ;  
  
2. Acesse o Módulo Gestão de Pessoal / Relatórios / Provisões / Provisão de Férias ou Provisão de13º Salário. Na aba Ordem, Selecione a opção Centro de Custo, e preencha os parâmetros para emissão do Relatório de Provisão:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10410389898135)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10410466102679)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10410468784663)  
  
3. O Relatório de Provisão será apresentado com os Totais de Cada Centro de Custo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10410634762775)

4. Realize o Processo de Contabilização das Provisões. Acesse: Miscelânea / Fechamentos / Contabilização:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10410814088599)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10410835367959)

5. Com os Lançamentos Contábeis em tela, acesse Outras Ações / Exp. Excel:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10411795871127)  
  
6. Filtre as Verbas que deseja realizar as conferências e faça um comparativo das verbas apresentadas no relatório os lançamentos contábeis apresentados na planilha:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10412135809303)

Observações: Veja que os valores negativos na provisão, ficam positivos na contabilização e que se a conferência é realizada por Centro de Custo, os valores ficam corretos.

7. Se a conferência for realizada utilizando os Totalizadores do Relatório de Provisão, o sistema poderá presentar diferenças:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10412149599639)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10412276238359)

Neste exemplo, inserimos um filtro por verba, e somamos os valores de cada verba de todos os centros de custos e comparamos com os valores dos Totais do Relatório de Provisão.  
  
Veja que, os valores contabilizados de INSS e FGTS de Férias não são iguais no Relatório e na Contabilização, pois com o conceito de contabilizar os valores negativos e inverter as contas contábeis, os valores negativos são somados na contabilização.  
  
A diferença corresponde exatamente ao dobro do valor negativo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10413321711127)

**Saiba Mais:**  
[Página Centralizadora da Contabilização Protheus RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
