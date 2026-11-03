---
content_hash: dcb115f67e9a5d49f06485be02a758b8867891bb9838beff1f84a53c8e8dd0fd
fetched_at: '2026-06-29T00:09:14.897730+00:00'
page_id: '421385298'
product: rm
source: tdn-rm
title: Composição do Tipo Equipamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385298
version: 2
---

---

Foram inseridas em recursos da composição as opções "Produtivo" e "Improdutivo", estas podem ser acessadas pela edição do recurso da composição ou através das colunas "Produtivo" e "Improdutivo" localizadas na visão de Composições / Anexos / Recursos da composição ou através da edição da composição grid recursos. Estas opções devem ser marcadas para serem utilizadas.

O "Produtivo" e "Improdutivo" podem ser marcados ao mesmo tempo, e após realizar o cálculo da composição o "Custo Produtivo" e o "Custo Improdutivo" poderão ser visualizados na edição da composição, caso estas fiquem desmarcadas estes custos não serão considerados.

O custo produtivo e improdutivo da composição será calculado da seguinte forma:

* Custo Produtivo: será definido pelo somatório da quantidade multiplicada pelo valor de cada recurso produtivo.
* Custo Improdutivo: será definido pelo somatório da quantidade multiplicada pelo valor de cada recurso improdutivo.

**Exemplo:**

Para a composição estão associados vários insumos:

* Insumo 1: Preço Unitário 10, quantidade 1, marcado apenas produtivo.
* Insumo 2: Preço Unitário 10, quantidade 1, marcado produtivo e improdutivo.
* Insumo 3: Preço Unitário 20, quantidade 1, marcado apenas produtivo.

Os custos serão:

* Custo Produtivo: ((1\*10) (1\*10)(1\*20)) = 40

(Quantidade do insumo \* Preço Unitário) dos insumos cujo "Produtivo" esteja marcado.

* Custo Improdutivo: (1\*10) = 10

(Quantidade do insumo \* Preço Unitário) dos insumos cujo "Improdutivo" esteja marcado.

Normalmente uma composição do tipo equipamento é utilizada como composição auxiliar de uma composição por produção, neste momento as opções de coeficiente produtivo e coeficiente improdutivo são apresentadas, nesta situação não é possível definir as opções "Produtivo" e "Improdutivo" da edição de recursos da composição, o cálculo da composição será feito com base nos coeficientes apresentados.

**Exemplo:**  
O preço do recurso é 10,00, a quantidade do recurso da composição é 2 e os coeficientes informados são coef. Produtivo = 0,8 coef. Improdutivo = 0,2.  
   
**Cálculo:**((coeficiente produtivo \* custo produtivo)+(coeficiente improdutivo \* custo improdutivo) quantidade do recurso na composição)\*(0,8\*10)+(0,2\*0)\*2 = 16 -> preço parcial  
   
**Exemplo:**

Neste exemplo será considerado que existe uma composição por produção, onde foi associada uma composição do tipo equipamento e esta composição possui um insumo de qualquer tipo. Foram informados para o recurso associado à composição por produção, no caso a composição do tipo equipamento o coeficiente. Produtivo = 0,8 coeficiente. Improdutivo = 0,2, quantidade igual a 2. Para o insumo associado à composição do tipo equipamento, foi definido que o custo improdutivo é calculado (a opção "Improdutivo" é marcada), ou seja, para a composição em questão existe um custo improdutivo de 10,00, isso porque o preço unitário do insumo associado é 10,00 e a quantidade deste na composição é 1. Portanto o seguinte o cálculo é realizado:  
   
**Cálculo:** (0,8\*10)+(0,2\*10)\*2 = 20 -> preço parcial  
   
**Exemplo:**

Em uma composição por produção, um insumo do tipo equipamento será associado, quantidade igual a 1, preço unitário igual a 10, coeficiente produtivo 0,8 e coeficiente improdutivo 0,2. Insumos do tipo equipamento utilizam coeficientes Produtivos e coeficientes Improdutivos, portanto a opção para definir o cálculo do "Produtivo" e "Improdutivo" não é habilitada.  
   
**Cálculo:** (0,8\*10)+(0,2\*0)\*1 = 8 -> preço parcial  
   
**Atenção:**

Na planilha de atividades o valor considerado para cálculo é o valor do recurso. Seguindo o exemplo 2 e considerando que a composição por produção esta associada a uma tarefa, onde a quantidade do recurso na tarefa é 10, o preço seria o seguinte:  
(10\*20) = 200 (Valor do Recurso \* quantidade da tarefa). Se a composição do tipo equipamento for associada a uma tarefa, o valor considerado para o cálculo também será o valor do recurso.  
  
**Observação:**

* Ficarão habilitadas as opções "Produtivo" e "Improdutivo" na edição de recursos da composição, apenas na composição cujo tipo for equipamento.
* Para recursos do tipo mão de obra é realizado apenas o cálculo do valor produtivo, que já é marcado como default.
* Os campos Custo Produtivo e Custo Improdutivo são habilitados apenas quando a composição for do tipo equipamento.
