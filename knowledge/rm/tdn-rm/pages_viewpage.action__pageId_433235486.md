---
content_hash: c5e3dd58a76405e0eb0e5e48d223891c4007f7737e220a3539f999fe163ec4a1
fetched_at: '2026-06-29T00:09:44.397058+00:00'
page_id: '433235486'
product: rm
source: tdn-rm
title: RMFIN000021_Codificação irregular no Cadastro de ClientesFornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433235486
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Financeira |
| **Versões:** | 11.0.7 |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | Sintoma  *Código do Cliente/Fornecedor com numeração desordenada no cadastro.*  Causa  Ao cadastrar um cliente/Fornecedor, não está sendo observada a informação do ultimo cliente ou Fornecedor já cadastrado e o código é informado sem nenhum critério.     Solução  Se a sequencia dos códigos do cadastro de cliente/fornecedor não estiver regular, a forma mais simples para ajustar é listar todos os clientes e Fornecedores e ordená-los por CODIGO. Ao cadastrar um novo, utilizar os códigos ainda não utilizados para completar a sequencia. Repetir esse processo a cada inclusão de Cliente/Forencedor até que a sequencia fique totalmente regular.  **Informações Adicionais**   1. A definição da máscara do cliente/fornecedor deverá ser feita na fase de implantação, pois a alteração da máscara com registros já cadastrados se trata de um processo complexo, que somente poderá ser feita por profissional com habilidades específicas e através do Banco de Dados.      1. Existem várias opções para a codificação do cadastro e o sistema fornece informações para orientar o usuário no momento de se atribuir a máscara (Através do Assistente de Implantação de Processos, etapa 02.01 – Cliente/Fornecedor, campo “Mascara do Código”). Posicionando o cursor sobre o campo “Mascara do Código” serão exibidas todas as combinações possíveis para a definição da mesma.      1. Desejando uma codificação seqüência (automática) no cadastro do cliente/fornecedor, defina a máscara para “Somente Números”. Esta operação deve ser realizada antes de iniciar a inserção de dados no cadastro de Clientes/Fornecedores.  1. O sistema armazena **o último** código cadastrado tanto para cliente quanto para fornecedor. Portanto, é muito importante observar essa informação para manter a ordem do cadastro.   Exemplo:   Cadastrando o F000313 = Fornecedor A Ao cadastrar o próximo será exibido o numero F000313 como sendo o ultimo Fornecedor cadastrado.   Se for informado um numero qualquer, por exemplo F000913, o sistema irá exibir esse numero como sendo o ultimo ao incluir o próximo. Perceba que a sequencia não foi mantida. |
| **Observações:** |  |
