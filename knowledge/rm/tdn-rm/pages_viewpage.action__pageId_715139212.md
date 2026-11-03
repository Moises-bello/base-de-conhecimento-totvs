---
content_hash: 667a08cbf38acd7876be49478117b05b3938fa058716608d0dca9203d4b2525b
fetched_at: '2026-06-29T00:11:25.685184+00:00'
page_id: '715139212'
product: rm
source: tdn-rm
title: COCKPIT 360 - Visão Cockpit
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715139212
version: 23
---

### Visão Cliente 360°

Na visão do Cockpit é possível visualizar a vida do cliente no TCGI, seja contratos de aluguel ou vendas, como visão financeira, contratos, atendimentos, cobranças e interesses em outros negócios.

Para realizar a busca, selecione o tipo de filtro a ser realizado como: o nome do cliente, contrato, subunidade, CPF e outros, para retornar a visão somente de um único cliente, independente do tipo de filtro todos retornaram o cliente. Depois desse filtro é possível pesquisar um subfiltro dentro desse filtro, como um empreendimento específico desse cliente ou até mesmo um contrato específico.

Para retornar a composição dos valores é possível marca a opção de buscar a posição atual da base, sem marcar nenhum parâmetro ou atualizar o valor líquido do financeiro com base na data, podendo considerar o deságio e multa/juros, dessa forma os valores ficaram semelhantes a ficha financeira, desde que comparada com a opção atual ou atual reajustada

Importante!

Caso haja parcelas de financiamento ou parcelas de despesa parcialmente quitadas (baixa parcial) o sistema irá exibir estas parcelas nos cards de parcelas em atraso ou parcelas futuras, conforme a situação dela e irá exibir e contabilizar as baixas parciais destas parcelas no card de parcelas pagas/parcial.

Ao pairar o mouse sobre este card, o sistema exibirá a mensagem abaixo, de acordo com a quantidade de baixas parciais das parcelas:

*Tem # baixas parciais para o cliente, com isso a quantidade dessas parcelas parciais será dobrada, pois apresentará em aberto e pagas*

Por exemplo: Considerando que o Cliente tem apenas 1 parcela de financiamento em atraso, com 3 baixas parciais. O sistema irá exibir os cards da seguinte forma:

* 1 Parcela em Atraso: com o valor do saldo devedor desta parcela;
* 3 Parcelas Pagas/Parcial: com a soma dos valores das 3 baixas realizadas na parcela;

O mesmo comportamento ocorrerá para as parcela de despesa.

Após carregar os dados desse *Cliente*, é possível de se refinar a pesquisa, filtrando o *Empreendimento* ou *Imóvel* e também o *Contrato* a ser detalhado.

**Na visão do Cockpit , é informado o Número da Venda e o Número do Contrato que é diferente do número da Venda.**

Para que o usuário consiga visualizar o valor **financeiro atualizado (considerando juros, multa e reajuste online)**, no cockpit tem um Flag que atualiza esse valor em todos os valores apresentados que justifiquem essa atualização na data de hoje.

É permitido filtrar somente cliente ativo no contrato, que tem participação >=0 e esteja sem data hora de saida

Relatórios Genéricos

Através do cockpit agora , é possível solicitar a emissão de um relatório genérico, além dos relatórios já disponíveis (ficha e IR).

No menu da grid de contrato foi disponibilizado o Gerador de relatório por contrato de venda/aluguel

Cockpit se consegue gerar  relatórios gerais do tipo 92 e do TCGI, o relatório tem que ter o contexto da venda **(xVenda)** e Aluguel **(xAlgContratoAlg)**

Os relatórios vem com o padrão já preenchidos .

EM TEMPO:

*\**Há cenários em que a tela do RM é redimensionada automaticamente ao se acessar o *Cockpit 360°*.

Esse comportamento ocorre quando o Microsoft Windows está configurado para usar uma *Escala* de Tela diferente de **100%**.

Se necessário, altere essa configuração no Windows e verifique qual delas é a melhor para o seu cenário.

[Clique aqui](https://learn.microsoft.com/pt-br/visualstudio/designers/disable-dpi-awareness?view=vs-2019) para maiores detalhes

**Para corrigir este cenário, siga os passos abaixo:**

1. Localize o arquivo *RM.exe,* que geralmente está na pasta C:\TOTVS\CorporeRM\RM.Net;
2. Clique com o botão direto do mouse neste arquivo e acesse *Propriedades*;
3. Na janela de *Propriedades*, acesse a aba *Compatibilidade*;
4. Nesta aba, clique no botão *Alterar configurações de DPI alto*;
5. Na janela *Configurações de DPI alta para RM.exe*, marque a opção *Substituir o ajuste de DPI*;
6. Na opção Ajuste executado por, selecione a opção Sistema;
7. Clique no botão OK para aplicar esta configuração; e
8. Feche a janela de *Propriedades do RM.exe.*
