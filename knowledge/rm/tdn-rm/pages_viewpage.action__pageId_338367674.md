---
content_hash: 7b63353e901e3393e78e0ead01ed217f84a6aafb49993a19e523e0ca6a4f0b0e
fetched_at: '2026-06-29T00:08:51.850419+00:00'
page_id: '338367674'
product: rm
source: tdn-rm
title: FOP_ROTINAS Configurando Margens Relatório .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338367674
version: 89
---

# Configurações Para Ajustar Tamanho das Margens do Relatório de Informe de Rendimentos

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Versões:** | 12.1.17.222 ou Superiores  12.1.18.143 ou Superiores  12.1.19.101 ou Superiores |
| **Ocorrência:** | Como fazer para configurar tamanho das margens em relatórios .Net, como por exemplo o Informe de Rendimentos, que em alguns casos podem sair com mais de uma página, dependendo da quantidade de informações do funcionário e do tamanho configurado para as margens. |
| **Ambiente:** | Gerador .Net / Informe de Rendimentos |
| ****Observações:**** | Apesar deste documento estar focado no Informe de Rendimentos, essa configuração é válida para qualquer relatório .Net. |
| **Passo a passo:** | Em alguns casos ao emitir o relatório de Informe de Rendimentos dependendo da quantidade de informações do funcionário, o relatório poderá ser quebrado em duas páginas. Uma das maneiras para evitar que isso ocorra é diminuir o tamanho das margens do relatório (principalmente superior e inferior). Diminuir o tamanho das margens não garante que todos os funcionários terão o informe de rendimentos em apenas uma página, pois, se a quantidade de informações do funcionário for muito grande, mesmo configurando as margens ele sairá em duas ou mais páginas.    Para alterar os tamanhos das margens nos relatórios em .Net é necessário que você faça o ajuste na estrutura do relatório, em Gerador .Net (Reports).    Acesse o caminho:  **(RM Labore.exe)** Relatórios | Gerador .Net | Selecione o Relatório desejado | Processos | Editar Estrutura    **(RM.exe / MDI)**  Gestão | RM Reports | Folha de Pagamento | Selecione o Relatório desejado | Processos | Editar Estrutura        Caso seja apresenta a mensagem abaixo, informando que você não tem permissão:        Será necessário que você exporte o relatório “Processos | Exportar Estrutura de Relatório” e em seguida importe a estrutura “Processos | Importar Estrutura de Relatório” alterando o código do relatório, pois, para garantir a integridade os relatórios padrões não permitem alterações. Ao importar com outro código o relatório deixa de ser padrão TOTVS e passa a ser um relatório personalizado, permitindo qualquer alteração desejada.    **Estrutura do Relatório .Net**        O gerador Report está configurado em Decímetros, exemplo: 2cm vai estar como 200. Ele utiliza o drive da impressora para considerar o tipo de papel definido pela mesma ou então o que foi personalizado no servidor de aplicação da impressora.  Então no gerador acesse:    **- Propriedades do Relatório**  Basta clicar com o botão direito do mouse fora da estrutura do relatório e em seguida selecionar Propriedades        **- Alterando as margens do relatório:** Nas propriedades do relatório > Definições de Página > Margens.      Direta: Margem direita do relatório; Esquerda: Margem esquerda do relatório; Fundo: Final do relatório (rodapé); Topo: Inicio do Relatório (cabeçalho).  Exemplo: O valor 156 da margem esquerda do relatório, significa aproximadamente 1,5 cm de margem a direita.    Então basta reduzir estes números conforme desejado para que as margens sejam alteradas.  Após alterar as margens, você deve clicar no botão “Salvar” localizado no alto da página de edição do relatório e depois basta informar o relatório editado para geração do informe de rendimentos: |

divs
