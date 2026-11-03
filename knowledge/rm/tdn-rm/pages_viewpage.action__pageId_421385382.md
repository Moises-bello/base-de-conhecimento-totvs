---
content_hash: e79f543a885174006b6b641ee4cf5ba601bb82144834ea236a0d910df9c79f50
fetched_at: '2026-06-29T00:09:15.447125+00:00'
page_id: '421385382'
product: rm
source: tdn-rm
title: Composições (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385382
version: 3
---

---

**Calcular Composição ao Salvar:** com este parâmetro selecionado, ao se incluir uma composição e salva-la, o cálculo da composição é realizado.

**Bloquear a digitação Manual das fórmulas de produção:** com este parâmetro selecionado, a digitação manual das fórmulas de produção é bloqueada.

**Considerar a utilização de preço improdutivo na CPU:** Este parâmetro modifica o calculo do custo improdutivo da CPU, na existência de recursos definidos como improdutivos que sejam insumos será considerado o preço improdutivo definido no mesmo. Com este parâmetro desmarcado entende-se que o preço parcial é o custo improdutivo deste insumo.

Exemplo:

CPU - CAM. BASC.20M3 8x4

Recursos - Improdutivos

                                         - TIPO

IH1001 MOTORISTA - CPU

Custo Improdutivo - R$14,50

IP1001 CUSTO PROPRIEDADE-CAM. BASC.20M3 8x4    - INSUMO

                                               Preço Parcial - R$140,00

Preço Improdutivo - R$110,00

Total improdutivo da CPU CAM. BASC.20M3 8x4 será:

Parâmetro marcado: R$124,5

Parâmetro desmarcado:  R$154,5

Ou seja com o parâmetro marcado será necessário o cadastro de preço Improdutivo para os insumos, já com o parâmetro desmarcado o preço improdutivo e parcial será o mesmo.

**Aplicar quantidade 0 (zero) na associação de recursos na composição por padrão:** com este parâmetro selecionado é possível definir se o padrão da quantidade na associação de recursos na composição será 0 (zero) ou 1 (um), ou seja, se este for selecionado, a quantidade na tela de associação de recurso à composição, passará a ser '0', ou invés de '1', e se estiver desmarcado abrirá a quantidade igual a 1.

Ao adicionar um recurso na composição, o padrão da quantidade atualmente é 1 (um). Para que o usuário possa definir se o padrão da quantidade na associação de recursos na composição será 0 (zero) ou 1 (um), basta observar o parâmetro 'Aplicar quantidade 0 (zero) na associação de recursos na composição por padrão' através do menu Projeto | Construção e Projetos | Projetos (F6) | aba Composições, ou seja, se este parâmetro for selecionado, a quantidade na tela de associação de recurso a composição, passará a ser '0', ou invés de '1', e se estiver desmarcado abrirá a quantidade igual a 1.

**Observação**  
Nas importações de Composição é necessário observar a quantidade de um recurso importado, pois se o valor no arquivo a ser importado vier vazio, o sistema guardará o valor conforme estiver parametrizado no projeto. Assim ao importar alguma composição e a quantidade do recurso associado estiver vazia, esta quantidade recebe o que está definido em seu padrão na tela de parâmetros do projeto.
