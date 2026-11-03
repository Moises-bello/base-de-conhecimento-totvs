---
content_hash: 62bdc3ce4d12b47de882a8447a76e7ae7ad3326bddae07121d84f8fb4a2f473d
fetched_at: '2026-06-29T00:09:28.704633+00:00'
page_id: '423938762'
product: rm
source: tdn-rm
title: Relatório (Livro Registro de Inventário)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938762
version: 2
---

O Livro Registro de Inventário tem o objetivo de registrar todos os produtos em estoque quando realizado o levantamento do balanço da empresa.  
 O relatório disponível no sistema RM foi desenvolvido para exibir o Saldo por Local de Estoque em uma determinada data.   
 Para utilizá-lo é necessário acessar Gestão | RM Reports | Processos | Importar Estrutura de Relatório | Navegar até a pasta de instalação da Biblioteca RM (C:\totvs\CorporeRM\ObjetosGerenciais\Relatórios) | Selecionar o arquivo NUCREL00046 - Livro Registro de Inventário.TotvsReport e importa-lo.  
 Após a importação do relatório, é possível obter os registros das mercadorias em estoque selecionando o mesmo na visão | Processos | Gerar Relatório.  
 Na execução do relatório é possível informar os seguintes parâmetros:

* **Data do Inventário:** Data que o inventário está sendo realizado.
* **PRD\_INI:** Código do produto inicial.
* **PRD\_FIM:** Código do produto final.
* **DATA\_D:** Data limite de movimentação que se deseja gerar o relatório.
* **Código da Filial:** Código da filial.
* **Local de Estoque:** Código do local de estoque da filial informada.

***Observação***: Não é possível selecionar várias filiais e locais de estoque para a geração do relatório padrão disponibilizado.
