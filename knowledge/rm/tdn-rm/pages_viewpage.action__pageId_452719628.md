---
content_hash: e888ee2a062094c8d41d35027c194b8564f6567ffe35d8a3a635320d37d43565
fetched_at: '2026-06-29T00:10:09.319481+00:00'
page_id: '452719628'
product: rm
source: tdn-rm
title: Alteração de Tomadores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719628
version: 3
---

A informação de tomadores de serviços no cadastro de funcionários serve para gerar o arquivo de SEFIP.RE e pode ter alterações periódicas. A manutenção pode ser feita no cadastro do funcionário diretamente de forma rápida se for somente alguns.   
    
 A rotina de alteração global de tomadores será útil caso haja necessidade de alterar um número maior de funcionários.  
    
 A consistência de dias informados por tomador de serviços para cada funcionário será feita gerando um log com inconsistências dos dias a distribuir x total de dias distribuídos, ou seja, será mostrado todos os funcionários que ultrapassaram os dias de trabalho em determinado mês.  
    
 De acordo com a seleção utilizada, a rotina modifica os campos que são solicitados. Dentro desta seleção, sobrescreverá qualquer outra informação relativa à distribuição por tomadores  no cadastro de funcionários pela informação especificada na rotina, ou seja, se existirem tomadores de serviço cadastrados nas respectivas pastas dos funcionários, estas informações serão apagadas e no lugar destas serão incluídas as informações cadastradas neste módulo. Com este módulo, será possível determinar a configuração de tomadores a ser adotada para uma quebra ou filtro especificado.

**Atenção:**

Tenha muita atenção para esta alteração porque será cadastrado tomador de serviços para todos os funcionários do filtro selecionado. Poderá ser alterados apenas dias de distribuição, caso não seja necessário a alteração do tomador de serviços. Neste caso somente será aceito um código que está sendo utilizado no Cadastro dos Funcionários em Tomadores de Serviços.

**Observações:**

1. Se não informar nenhum tomador a alteração será realizada para todos os tomadores de serviços cadastrados no registro do funcionário. As informações de De/Para somente estarão disponíveis para alteração de apenas dias de distribuição. Confira o exemplo De/Para .  
     
   **Observação:** A informação de De/Para será convertida para "Tipo" quando for solicitado "Determinar distribuição a todos os funcionários processados" para a seleção de qual "Tipo" de Tomador de serviço será marcado dentro da pasta de tomadores de serviço do funcionário.
2. A alteração dos dias a serem distribuídos pelo tomador pode ser feita através de fórmula, como por exemplo, considerando os dias trabalhados do funcionário em determinado mês, deverá montar uma fórmula com o valor = ND. Confira o exemplo Fórmula ND   
   Dicas:   
   1.    Alteração de 30 para 31 dias em empresas que tem funcionários horistas e mensalistas.  
   2.    Alterações de dias utilizando a formula ND para funcionários ativos, afastados no mês, retornos de afastamento, férias no mês, admitidos no mês e etc.
3. Caso possua algum tomador que tenha data inicio anterior a competência atual, o processo irá criar uma data fim para esse tomador, para preservar o histórico e criará um novo com data atual.
4. Caso o tomador selecionado no processo não exista no cadastro de Lotação Tributaria, será disparado um gatilho de inclusão.
