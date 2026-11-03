---
article_id: 360025817211
category: RH - Sindicais
content_hash: 85aac7c416a99c592ce39fe9752d07fa59fd122b622eb016c7f037dff2d18b2e
fetched_at: '2026-06-28T22:43:10.892057+00:00'
product: protheus
section_id: 360011997333
source: central-protheus
title: RH - Linha Protheus - GPE - Como definir se será calculada as contribuições
  confederativa, assistencial e mensalidade sindical para empregados afastados
type: support-article
updated_at: '2025-04-11T16:35:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025817211-RH-Linha-Protheus-GPE-Como-definir-se-ser%C3%A1-calculada-as-contribui%C3%A7%C3%B5es-confederativa-assistencial-e-mensalidade-sindical-para-empregados-afastados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24797856579607) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como definir se será calculada as contribuições confederativa, assistencial e mensalidade sindical para empregados afastados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para que o sistema não calcule as contribuições assistencial, confederativa e mensalidade sindical de acordo com os dias de afastamento para os empregados afastados, deixe o mnemônico **P\_PROPCONT** com **.T.**. Para configurar o mnemônico acesse: **Atualização > Definição de calculo > Mnemônico (GPEA300)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24797856584087)  
  
Caso o conteúdo desse parâmetro esteja com valor **Falso** **(.F.)** o sistema **irá efetuar o cálculo** independentemente da configuração que exista no cadastro de Sindicato aba **Outras informações**, campo  **Desc.Afast**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24797856587927)  
  
Desmarque as contribuições que não deseja calcular no campo **Desc. Afast.** no cadastro de sindicato, acessando **Atualizações > Cadastros > Sindicatos (GPEA340):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24797901654295)

O campo  **Desc. Afast**. (RCE\_DESAFA) no cadastro do Sindicato, tem a opção de escolha entre quais contribuições será realizado o desconto para o empregado afastado, se selecionada a contribuição no campo, o desconto será feito na folha do funcionário afastado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24797856600599)

Além da configuração do sindicato e mnemônico **P\_PROPCONT**, o sistema também valida o mnemônico **P\_NDAFAACS**, onde irá considerar os dias informados nele para definir se irá descontar ou não as contribuições para os funcionários afastados, exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24797856603927)  
  
Então, para os funcionários com **afastamentos menores** que a quantidade informada no mnemônico **P\_NDAFAACS**, o cálculo das contribuições **será realizado**, e para os funcionários com **afastamento maior,** o desconto **não será realizado**.  
  
**IMPORTANTE:** O sistema somente irá validar funcionários onde o campo SIT FOL estiver com A. E é necessário a configuração correta conforme a necessidade tanto de Sindicato como de mnemônicos.

**Saiba Mais**  
Para adquirir maior conhecimento acesse os *link*s abaixo

[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)  
[Artigos sobre contribuições sindicais](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011997333-RH-Sindicais)  
[Calculo das contribuições: Assistencial, Confederativa e Mensalidade Sindical para funcionários afastados](http://tdn.totvs.com/display/public/PROT/417367+MRH-6040+DT+contribuicoes+Assistencial%2C+Confederativa+e+Mensalidade+Sindical)
