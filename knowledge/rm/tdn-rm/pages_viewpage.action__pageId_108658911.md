---
content_hash: 8d52aed40dc22c75af89b11dc761229424e72d3d311085d33f4dc7dd8a0c5e51
fetched_at: '2026-06-29T00:05:54.768005+00:00'
page_id: '108658911'
product: rm
source: tdn-rm
title: Parametrização da Geração de Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=108658911
version: 7
---

|  |
| --- |
| **Produto:** *TOTVS Educacional*                                   **Versão:** *11.50* |
| **Processo de Negocio: Geração de acordo**  **Processo do Sistema: Parametrização e entendimento do processo** |

 ***Não foi possível gerar o acordo. Favor preencher o parâmetro “Serviços parametrizados para não verificar inadimplência” no TOTVS Educacional.***

É muito comum presenciarmos questionamentos com relação ao erro acima. Na maioria das vezes sabemos como corrigir, mas não sabemos o funcionamento correto do processo.

Veja a exemplificação abaixo para entender como o parâmetro funciona:

Em opções --> Parâmetros --> Educacional --> Tesouraria, temos o parâmetro "Agrupar lançamentos de serviços com tratamento diferente de inadimplência".

Este parâmetro trabalha da seguinte maneira:

1 - Quando marcado será habilitado um único campo para preenchimento do "Serviço:". Nele será selecionado um serviço cadastrado no sistema para que os lançamentos gerados, através de acordo, sejam gerados com esse registro cadastrado.

*Exemplo: Campo parametrizado como serviço "Acordo Geral".*  
*Aluno possui três (3) parcelas, uma para o serviço Material (Não verifica inadimplência) e duas para o serviço Mensalidade (Verifica inadimplência).*

*Nesse caso, todas as parcelas que forem geradas para um possível acordo, das 3 parcelas citadas anteriormente, terá o serviço parametrizado "Acordo Geral".*  
*Obs.: Para verificar se o serviço verifica ou não inadimplência:*  
*Cadastro --> Financeiro --> Serviço --> Editar serviço --> parâmetro --> "Verifica inadimplência durante o processo de matrícula."*

2 - Quando Desmarcado, será habilitado dois campos para preenchimento: "Serviço parametrizado para verificar inadimplência" e "Serviço para NÃO verificar inadimplência."  
É necessário o preenchimento de um serviço em cada um dos campos para que o processo ocorra perfeitamente.

*Exemplo: Campo: "Serviço parametrizado para verificar inadimplência” parametrizada com: "Acordo verifica inadimplência".*  
*Campo: "Serviço para NÃO verificar inadimplência” parametrizada com: "Acordo não verifica inadimplência".*

*Aluno possui três (3) parcelas, uma para o serviço Material (Não verifica inadimplência) e duas para o serviço Mensalidade (Verifica inadimplência).*  
*Nesse caso, será necessário gerar acordo para as parcelas com serviço Material que terão suas parcelas preenchidas com o serviço Acordo não verifica inadimplência, e depois será gerado um acordo para as parcelas com o serviço "MENSALIDADE" onde as parcelas serão preenchidas com o serviço "Acordo verifica inadimplência".*

Apenas na versão **12.1.2302**, em Parâmetros --> Educacional --> Integração --> Financeiro --> Educacional - Etapa"Geral - Fin 4/4", foi implementado o parâmetro "Tipo parcela do acordo", com as opções:

Parcela adicional: Essa é a opção padrão do sistema, quando selecionada as parcelas do contrato de tipo acordo serão do tipo adicional.

Parcela extra: Quando selecionada as parcelas do contrato de tipo acordo serão do tipo extra.
