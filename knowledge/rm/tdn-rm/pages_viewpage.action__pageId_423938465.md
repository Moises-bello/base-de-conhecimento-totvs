---
content_hash: 84a2a7b9d5c245426b9b0e20663985974918db15f7234b159ba9c20bba9ec3d0
fetched_at: '2026-06-29T00:09:27.261340+00:00'
page_id: '423938465'
product: rm
source: tdn-rm
title: Importação de Contas via Arquivo texto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938465
version: 5
---

Visando facilitar a preparação do ambiente para geração das rotinas legais ECF, ECD e FCONT, o sistema disponibiliza o processo que permite a importação de arquivos textos dos planos de contas referenciais, estes publicados pela Receita Federal.

Para que a importação seja realizada com sucesso, é necessário selecionar previamente a "capa" para onde deseja importar as contas paralelas ou informar o código desta diretamente no campo "Plano de Contas (Capa)". Ou seja, antes de executar o processo é obrigatório que uma capa do Plano de Contas Referencial seja criada e não poderá ser informado neste campo uma capa que já tenha contas paralelas.

Ao realizar o cadastro da Capa o sistema irá exigir o preenchimento do campo "máscara". O usuário não tendo certeza desta informação, basta informar a máscara que desejar e no momento da importação marcar a opção "Identificar/Atualizar máscara automaticamente?". O Sistema irá identificar a máscara do plano de contas referencial que está sendo importado e atualizar essa informação na Capa do Plano Referencial.

No campo "arquivo" é necessário informar o diretório onde está disponível o arquivo texto contendo as contas paralelas a serem importadas. A validação da importação pode ser feita selecionando a capa do plano referencial e acessando Anexos| Contas Paralelas.

Sabemos que alguns planos de contas referenciais publicados pela Receita Federal possuem contas analíticas e sintéticas no mesmo nível de máscara. Para isso foi disponibilizada a opção "Não validar níveis da máscara? ", que possibilita o usuário realizar a importação desse tipo de plano de contas sem que seja apresentada mensagens de validação referente aos níveis de máscara.

**Layout**

O layout do arquivo será identificado na primeira linha do arquivo de importação, ele determinará a posição dos campos e o separador de campos. Quando esta linha não for informada o sistema vai considerar o layout default.

**Configuração da Linha**

A linha a ser informada deve seguir o exemplo abaixo.

Exemplo

LAYOUT|CODCONTA=1|DESCRICAO=2|DATAINIVIGENCIA=3|DATAFINVIGENCIA=4|ANALITICA=5|SEPARADOR=| A linha de layout sempre utilizará o caractere "|" como separador

A palavra "LAYOUT" indica ao sistema que é para considerar como layout as informações prestadas na linha. Os campos a serem importados serão identificados entre os separadores "|", logo na frente do campo é identificada sua respectiva posição na linha do arquivo a ser importada. O separador de campos no arquivo deverá ser informado logo após a palavra "SEPARADOR", caso não seja informado o sistema irá considerar o caractere "|" como separador.

**Layout default**

LAYOUT|CODCONTA=1|DESCRICAO=2|DATAINIVIGENCIA=3|DATAFINVIGENCIA=4|ANALITICA=5|SEPARADOR=|

Exemplo da linha utilizada nos arquivos do SPED/ECF

LAYOUT|CODCONTA=1|DESCRICAO=2|DATAINIVIGENCIA=3|DATAFINVIGENCIA=4|ANALITICA=6|SEPARADOR=|

Havendo necessidade e respeitando as regras do sistema, é possível também realizar a cópia de plano de contas paralelo entre coligadas, já com a correta vinculação entre plano de contas contábil, plano de contas referencial e contas gerenciais/centro de custo.
