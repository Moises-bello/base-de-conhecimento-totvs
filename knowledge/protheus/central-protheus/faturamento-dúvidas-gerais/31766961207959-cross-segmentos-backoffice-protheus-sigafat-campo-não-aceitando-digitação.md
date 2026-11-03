---
article_id: 31766961207959
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 12e01096d8214769a4b9e289f47e9e4adb2723d31943780a77b15f6996aaee22
fetched_at: '2026-06-28T22:38:28.780253+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Campo não aceitando digitação
type: support-article
updated_at: '2025-04-30T17:40:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31766961207959-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Campo-n%C3%A3o-aceitando-digita%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31766961178903) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Um campo não está aceitando digitação, como resolver?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Caso esteja tentando inserir valor em um campo e, ele não está nem aceitando digitação (diferente de digitar, dar Enter e o sistema não aceitar), isso significa que:

1. Tem uma validação dentro do campo "Edição (X3\_WHEN)"  
   Caso o campo seja de cabeçalho, além não aceitar digitação, ele ficará acinzentado.  
   Caso o campo seja de itens, ele não muda de cor, só não aceita a digitação.
2. Tem propriedade "2 - Visualizar", campo "Propriedade (X3\_VISUAL)"

Essas validações, ficam na tabela "SX3 - Dicionário de campos", dentro do campo "Edição (X3\_WHEN)".

1) Aperte no campo ao lado do campo travado, em algum campo destravado, e aperte F1 para ver o nome do campo (para sabermos a qual tabela ele pertence). Se o nome do campo for por exemplo "AFG\_TESTE", o nome da tabela é "AFG", se for por exemplo "A1\_NOME", a tabela é "SA1", guarde o nome da tabela.

2) Para visualizar, vá no caminho: "Configurador (SIGACFG)" > "Base de Dados" > "Dicionário" > "Base de dados".

3) Expandir > Ir em dicionário de dados > Lupa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766961179671)

4) Pesquisar pela tabela pega no passo 1 > clicar no botão "Buscar" > Ícone de edição

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766961181207)

5) Expandir > Campos > Procurar pelo nome do campo travado e selecionar ele

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766961181719)

6) Depois de achar, clicar em edição

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766961182615)

7.1) Na janela aberta, na aba "Campos", é possível ver se o campo tem a propriedade travada (que seria 2 - Visualizar), ou seja, independe de tudo, esse campo nunca seria destravado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766961182743)

**Para resolver isso, se ele for destravado, ele pode ser alterado para "1 - Alterar", depois, salve as alterações.**

7.2) Na janela aberta, vá na aba "Opções" e veja o campo "Modo Edição (X3\_WHEN)", caso ele esteja com algum valor, aquela função ou fórmula é a responsável por "bloquear" o campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766993705367)

Quando a expressão/fórmula retorna verdade, o campo é destravado para aceitar valores de digitações na rotina.

**OBSERVAÇÃO 1:** Se a validação "Modo Edição (X3\_WHEN)" for padrão, não deve ser retirada.

**OBSERVAÇÃO 2:** Se não houver valor no campo "Edição (X3\_WHEN)" e a propriedade não for "2 - Visualizar" significa que o suposto travamento de digitação é feito via código-fonte, decidido assim para manter a integridade.
