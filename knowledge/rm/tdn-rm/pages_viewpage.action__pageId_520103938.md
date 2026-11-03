---
content_hash: e2f9084b32cdcc43c909c34784c0d720f74333c0e42d82bc7bd7629b775b9648
fetched_at: '2026-06-29T00:10:30.530404+00:00'
page_id: '520103938'
product: rm
source: tdn-rm
title: RMPAT00003_Relatório de Depreciação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520103938
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.14 Ou superior |
| **Ocorrência:** | Relatório de Depreciação |
| **Ambiente:** |  |
| **Passo a passo:** | O Relatório de Depreciação permite conferir individualmente os valores de depreciação calculados para cada um dos patrimônios. Através deste menu é possível emitir informações agrupadas por grupo de patrimônio, conta contábil, centro de custo ou filial.  **Regras para emissão do relatório** Como pré-requisito para composição deste relatório, deverão ser importados através do [RMReports](https://tdn.totvs.com/pages/viewpage.action?pageId=286747760) os arquivos abaixo: PATREL0014 - Relatório de Depreciação PATREL0015 - Relatório de Depreciação por Centro de Custo PATREL0016 - Relatório de Depreciação por C. Custo (Sintético c Contas) PATREL0017 - Relatório de Depreciação por C. Custo (Sintético) PATREL0018 - Relatório de Depreciação por Filial PATREL0019 - Relatório de Depreciação por Filial (Sintético c Contas) PATREL0020 - Relatório de Depreciação por Filial (Sintético) PATREL0021 - Relatório de Depreciação (Sintético)  Esses arquivos funcionam como layout para apresentação das informações, e estarão disponíveis no diretório de instalação: totvs\CorporeRM\ObjetosGerenciais\Relatórios.      **Emissão do Relatório de Depreciação** Acesse o menu Relatórios/Integrações | Depreciação. Inicialmente deve ser informado o mês e ano, respectivamente, desejado para apuração (período de apuração), quais patrimônios serão envolvidos (os ativos e/ou inativos) e o cenário de cálculo correspondente a estes patrimônios. Caso seja necessário, pode-se selecionar uma ou mais filiais. Desta forma somente as informações dos patrimônios existentes nas filiais selecionadas serão exibidas. Caso não seja selecionada filial, o sistema exibirá informações de todas as filiais, conforme o restante da parametrização.     O usuário poderá Selecionar o Status das Depreciações que deseja exibir: Não contabilizadas: Serão exibidas com o status contabilização “N” Não Integrada: Serão exibidas com o status contabilização “CN” Integradas: Serão exibidas com o status contabilização “CI” Contabilizadas: Serão exibidas com o status contabilização “C”  Caso não seja selecionado o status de contabilização, o sistema exibirá informações de todas as depreciações, conforme o restante da parametrização. A maneira como as informações serão pesquisadas é **extremamente importante para que os dados mantenham sua integridade**. Sendo assim, ao avançar etapa o usuário poderá filtrar por um ou mais grupos de patrimônio. Caso não seja selecionado grupo de patrimônio, o sistema exibirá informações de todos os grupos.    Antes de emitir o relatório é necessário selecionar o layout do relatório de depreciação que deseja. O usuário poderá também exibir depreciações de avaliações patrimoniais, através da opção 'Imprime Avaliações/Reavaliações patrimoniais'.    Ao avança e executar a emissão do relatório será apresentada: |
| **Observações:** |  |
