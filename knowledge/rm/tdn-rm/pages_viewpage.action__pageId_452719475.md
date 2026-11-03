---
content_hash: 2c9c328de792cf088fa28a0ba397d46a304326127a4551b25dabce791ae5efa7
fetched_at: '2026-06-29T00:10:07.929981+00:00'
page_id: '452719475'
product: rm
source: tdn-rm
title: Seleção de Lançamentos Ativos e Tabelas Opicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719475
version: 5
---

**Lançamentos Ativos**

Filtro das ocorrências financeiras que deverão ser impressas.  
**Exemplo:**  
Cadastrar lançamentos financeiros ativos (Tabela Dinâmica CODLANATIV)  na seguinte ordem:   
 1 - INSS  
 2 - Líquido Salarial - Filial SP  
 3 - Líquido Salarial - Filial RJ  
 4 - Líquido Rescisão  
   
Cadastrar também as seguintes parametrizações de lançamentos financeiros:  
   
 1 - Líquido Salarial - Todos os Funcionários  
  Tipo: 1 (Líquido Salarial)  
  Documento: 02 - Fatura  
  Cliente/Fornecedor: RM  
  Ocorrências Ativas: 2 e 3 (Líquido Salarial - Filial SP e Líquido Salarial - Filial RJ)  
   
 2 - INSS para todos os funcionários  
  Tipo: 4 (INSS a Pagar)  
  Documento: 12 - INSS  
  Cliente/Fornecedor: RM  
   Ocorrências Ativas: 1 - INSS  
   
De acordo com a seleção de campos, poderão ocorrer as seguintes possibilidades para a geração dos lançamentos financeiros:

* Se for selecionado na pasta Lançamentos Ativos o número 1 (INSS), somente será gerado a ocorrência financeira 2 (INSS para todos os funcionários).
* Se for selecionado, a ocorrência 1 e 2 (Líquido Salarial - Filial SP), as duas ocorrências gerarão lançamentos, uma vez que, a ocorrência 1 possui como ocorrências ativas com os códigos de cálculo 2 (Líquido Salarial - Filial SP) e 3 (Líquido Salarial - Filial RJ).
* Se for marcado somente o 4 (Líquido de Rescisão), não será gerado lançamento algum, pois nenhuma ocorrência financeira possui como lançamento ativo o valor 4.

O número de lançamentos a serem gerados depende da seleção de funcionários que foi feita. Haja vista, que o RM Fluxus não trabalha com o conceito de Seções, sendo assim, o RM Labore subdivide a quebra de seções em Filiais, Departamentos e Centro de Custos. Desta forma, o número de lançamentos gerados será igual ao número de registros obtidos com a quebra, multiplicados pelo número de ocorrências financeiras a lançar.  
   
**Observação :**  
Quando o usuário selecionar um lançamento ativo de IRRF (tipos: 5-IRRF a pagar, 8-IRRF de Férias, 9-IRRF de Rescisão, 12-IRRF 13º a pagar ou 20 – Total de IRRF) o sistema habilitará a pasta "Imposto de Renda" para informar o período de apuração.  
   
Ver mais detalhes em Imposto de Renda.  
   
**Tabelas Opcionais**   
   
Estas tabelas serão visualizadas caso o usuário as habilite no RM Fluxus nas Tabelas Opcionais existente na parametrização.  
Se o parâmetro "Usa parametrização" estiver desmarcado, o usuário poderá optar em selecionar o Código/Descrição de cada item das Tabelas Opcionais no momento da Geração dos Lançamentos Financeiros.   
Caso contrário, o sistema buscará as informações definidas nas Tabelas Opcionais na Parametrização dos Lançamentos Financeiros.  

---

[Voltar a pagina inicial](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719571)
