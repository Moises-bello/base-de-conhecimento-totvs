---
content_hash: 43e537e840c443dc1c8dc7c30466cd6a7956e1615eb7775c9583eead5e641afa
fetched_at: '2026-06-29T00:08:25.688626+00:00'
page_id: '270922450'
product: rm
source: tdn-rm
title: RMEDU00003_Geração de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270922450
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional TOTVS Gestão de Estoque Compra e Faturamento |
| **Versões:** | 12.1.14 |
| **Observações:** | Tem a finalidade de gerar movimentos no Educacional para posterior geração de NFe |

Referência para a criação do Tipo de Movimento:

<http://tdn.totvs.com/display/public/LRM/NFSE0004_Parametrizar_movimento_de_saida_para_NFS-e_mesmo_numero_da_Prefeitura>

TOTVS Gestão de Estoque, Compra e Faturamento

Acessar o TOTVS Gestão de Estoque, Compra e Faturamento

Ambiente | Parâmetros | Gestão de Estoque, Compra e Faturamento

·         Acessar o Parâmetros Outras Movimentações

**Observação: Estes passos deverão ser executados para os dois tipos de movimento, 2.1.xx e 2.2.xx.**

**1. Configuração dos movimentos** 

**Etapa Mov – Identificação:** 

Nesta Etapa Selecione a Serie para emissão de NFS-e (A série é definida pela prefeitura).

**Etapa Mov – Emitente/Destinatário 1/2:** 

Nesta Etapa o Emitente deverá ser “Empresa” e o destinatário “Cliente” ou “Fornecedor”

**Mov – Datas 1/2:** 

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Emissão”.

**Etapa Mov – Datas 2/2:** 

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Saída”.

**Item – Identificação 1/2:** 

Nesta Etapa pode ser selecionado o tipo dos itens, para a geração de movimento pelo Educacional o tipo deve ser “SERVIÇOS”

**Etapa Mov – Campos Livres 2/2:** 

Nesta Etapa pode ser selecionado a Edição do Histórico para Edita, este campo ira compor a TAG Discriminação do XML da NFS-e com as informações preenchidas no movimento.

**Etapa Fis - Tributação - Item:** 

Nesta etapa deve ser incluído o ISS para o item de movimento, definindo também o seu tipo de recolhimento. 

**Etapa Fis – Escrituração 1/2(Apenas para o movimento 2.2.xx):** 

Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento cadastrado para emissão de NFS-e.

**Etapa Fis – Escrituração 1/2(Apenas para o movimento 2.2.xx):** 

Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento cadastrado para emissão de NFS-e.

**Etapa Fis - NF-e:** 

Nesta Etapa deverá ser selecionado o Tipo de Envio da NFS-e Municipal (modelo Nacional), Manual ou Automático.

Avance até a última etapa salve os parâmetros do tipo de movimento.

Obs. Dúvidas com relação a criação e parametrização do Tipo de Movimento deverá ser esclarecida com a equipe de suporte do TOTVS Gestão de Estoque, Compre e Faturamento.

TOTVS Educacional

Acessar o TOTVS Educacional

Ambiente | Parâmetros | Educacional

Parâmetros Educacional | Integração – Fiscal 

Nesta Etapa vamos definir os parâmetros para geração o movimento.

**Integração – Fiscal 1/1:** 

Nesta Etapa deverá ser parametrizado a os dados para geração do movimento

**Utiliza Movimento por competência –** Com o parâmetro marcado o movimento é baseado na competência do contrato, dividindo o valor total pelas competências definidas no período letivo ou parametrização por curso.

Definição das competências:

**Data da competência –**O parâmetro defini de onde o sistema vai buscar a competência para a geração do movimento, podendo ser do Período Letivo ou a Parametrização do Curso.

Período Letivo

Parametrização por Curso.

Opções utilizadas somente com o parâmetro “Utiliza Movimento por Competência” marcado.

**Histórico –** Sistema disponibiliza algumas TAG’s para geração do histórico do movimento, no item do movimento deve ser utilizado o histórico longo.

**Integração – Fiscal 1/2:** 

Nesta Etapa deverá ser definido o valor para a geração do movimento

 Financeiro / Contábil – Serviços

Cadastro dos Serviços no TOTVS Educacional 

Verifique se o Produto criado no TOTVS Gestão de Estoque e Faturamento está vinculado ao serviço do TOTVS Educacional. Esta informação é obrigatória para geração de movimentos.

Editar o tipo de serviço do TOTVS Gestão de Estoque e Faturamento, basta clicar sobre a descrição do Serviço. Verifique as configurações do Serviço como mostrado abaixo:

Tipo: SERVIÇO e ULTIMO NÍVEL 

Na Aba ‘Informações por Filial’ verifique se a filial à ser utilizada para geração de movimento está informada.

Em Anexo - Tributos por Município, verifique se o Estado e Município estão informados de acordo com tributos. Verifique também o Código do Serviço no Município. Todos os tributos devem ser informados.

            Em Anexo - Dados Fiscais por UF, verifique se o estado está informado Salve o registro de serviço, caso tudo esteja corretamente configurado.

Currículo e Oferta – Alunos – Anexos Contratos

Currículo e Oferta – Alunos – Anexos Contratos

Editar o contrato – Anexos - Parcela

Gerar lançamento

Lançamento gerado com sucesso

Editar o lançamento clicando no código azul informado no campo Ref.

A tela de edição de lançamento será aberta

Acessar os anexos Boleto, verificar o IDBOLETO gerado para o lançamento

.

Financeiro **/** Contábil – NF-e – Geração de Movimento

Para gerar o movimento a partir do TOTVS Educacional, siga os passos abaixo:

Escolha o Tipo de Movimento criado anteriormente, escolha qual será a data, presente no Lançamento Financeiro, que será inserida como emissão do movimento.

No exemplo abaixo, ao clicar no filtro, criamos um filtro para digitação do IDBOLETO

Após execução, o movimento será gerado corretamente como pode ser visto no TOTVS Gestão de Estoque e Faturamento 

TOTVS Gestão de Estoque, Compras e Faturamento

Movimento gerado.
