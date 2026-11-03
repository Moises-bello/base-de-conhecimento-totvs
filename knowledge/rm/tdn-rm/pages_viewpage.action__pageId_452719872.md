---
content_hash: c4b7b4c28ce845357e782b6722e3c398a7df3dddd2d27b1312ad378bfef0ecb7
fetched_at: '2026-06-29T00:10:10.550528+00:00'
page_id: '452719872'
product: rm
source: tdn-rm
title: Informações de Rota e Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719872
version: 3
---

**Informações de Rota e Transporte**

Este anexo tem por objetivo armazenar os registros de informação de rotas (origem e destino da pessoa em relação ao local de trabalho) e transportes (linhas de coletivos e valor do transporte).

Aba Identificação:

ID Rota: código do registro de transporte/rota (ID da rota solicitada);

- Pessoa;

- Seção;

- ID Solicitação Integração: Código gerado pelo serviço de roteirização quando é solicitado um cálculo de rota. Este campo não será preenchido ao cadastrar uma rota manualmente;

- Data e Horário de atualização: data e horário da última atualização do registro, de acordo com a execução do processo Solicitar Cálculo de Rotas;

- Status: status da roteirização (Manual, Roteirizado, Não Roteirizado, Pendente);

- Motivos: de acordo com o resultado gerado pelo processo de Buscar Resultados de Roteirização; se o processo em questão não foi executado, este campo permanecerá em branco;

- Endereço de origem: endereço de origem da rota (CEP, logradouro, número, bairro, cidade e estado);

- Endereço de destino: endereço de destino da rota (CEP, logradouro, número, bairro, cidade e estado);

- Distancia total entre origem e destino.

- Tempo de deslocamento: tempo gasto de deslocamento

Ida – no percurso de ida;

Volta - no percurso de volta;

Total – no percurso de ida e volta.

- Valor (R$) gasto para deslocamento: valor gasto para deslocamento

Ida – no percurso de ida;

Volta - no percurso de volta;

Total - no percurso de ida e volta.

Nota: Quando os endereços de origem ou destino estiverem diferentes dos endereços dos respectivos cadastros de Pessoa e Seção será exibido uma mensagem de alerta na visão e edição de Informação de Rota e Transporte alertando que a rota traçada está desatualizada.

Aba Transporte(Anexo):

 -Linha: código e descrição da linha de transporte;

- Itinerário: itinerário feito pela linha

- Operadora: Nome da empresa operadora da linha;

- Tempo: Duração em minutos do tempo da viagem;

- Valor: Valor da tarifa do transporte;

- Sentido: Indicação do sentido do transporte na rota (ida ou volta);

- Sequência: Indicação da sequência do transporte, quando é necessário mais de um transporte coletivo para realizar um trajeto;

- Tipo: Tipo do transporte (Municipal, Intermunicipal);

- Cartão: Nome do cartão magnético de passagem;

- Valor Total (R$) gasto para deslocamento: valor gasto para deslocamento no percurso de ida e volta.

**Importante:**

 Este cadastro não irá alimentar os cadastros de Linha e Tarifa do TOTVS Folha de Pagamento, ou seja, no momento do cadastro os dados não irão para a folha de pagamento do funcionário.

Não haverá um cadastro de linha e tarifa, portanto, o ajuste de tarifa dos transportes será feito ao executar o processo "Buscar resultados de roteirização".

Somente registros que estejam com status 'Manual' poderão ter dados de informação de rota e transporte incluídos, editados ou excluídos manualmente. Para todos os outros status estas operações deverão ser bloqueadas.

|  |  |
| --- | --- |
|  | Informações Complementares |

Processo: Buscar resultados da roteirização|Buscar resultados da roteirização]
