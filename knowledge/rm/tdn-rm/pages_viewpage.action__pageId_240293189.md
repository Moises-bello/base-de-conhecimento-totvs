---
content_hash: 20391311213a4405c81b49fe249c06c03a439f2975a5859f10dee52b6dddd508
fetched_at: '2026-06-29T00:08:09.854880+00:00'
page_id: '240293189'
product: rm
source: tdn-rm
title: RMFIS00005_ECF Geração dos Registros X430 e X450
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240293189
version: 13
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 11.82.43 e 12.1.11(patches superiores) / Layout ECF: 08/06/2016 ou superior |
| **Ocorrência:** | Geração dos registros X430 e X450 |
| **Ambiente:** |  |
| **Passo a passo:** | Primeiramente, é necessário executar o script do registro [Y600](ftp://ftp.rm.com.br/Clientes%5CTEVOMJ53113791001790%5CECF/11_82/Script/) e o [X430/X450](ftp://ftp.rm.com.br/Clientes%5CTEVOMJ53113791001790%5CECF/11_82/Script/), propriamente.    **IMPORTANTE!** As informações serão providas pelo TOTVS Gestão Financeira. Portanto, para geração destes registros, é preciso possuir integração do Gestão Fiscal com o Gestão Financeira.    **Lançamentos Financeiros**.  Deve-se classificar todos os lançamentos financeiros quanto ao tipo da operação. Um campo foi criado na pasta “**Integração Fiscal**” do Lançamento Financeiro.      O mesmo está disponível no Processo de **Alteração Global**(Contas a Pagar/Receber -> Lançamentos -> Processos -> Manutenção de Lançamentos -> Alteração Global)**.**          **Escrituração Contábil Fiscal**  Para que os registros X430 e X450 sejam gerados na rotina, é necessário habilitar os campos “**Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior**” e “**Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior**”, respectivamente, em Anexos | Parâmetros da ECF, no Cadastro da Filial.        Assim como o campo "**Classificação do País**", na aba Identificação, deve ser informado.        Regra específica do **Registro X430:**   * Este será gerado se o campo “***Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior***” estiver marcado(Aba Complementares). * Serão selecionados todos os lançamentos financeiros a **receber** que estiverem com o campo **Classificação do Pagamento ou Recebimento** preenchido.     Regra específica do **Registro X450:**   * Este será gerado se o campo “***Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior***” estiver marcado (Aba Complementares). * Serão selecionados todos os lançamentos financeiros a **pagar** que estiverem com o campo **Classificação do Pagamento ou Recebimento** preenchido.     Regras comuns aos dois registros:   * Serão considerados os lançamentos de todas as Filiais, exceto as SCP’s. * Na ECF da SCP, serão considerados os lançamentos apenas daquela Filial. * Será gerado um registro para cada país movimentado durante o período da escrituração. * Os Lançamentos Financeiros selecionados devem ser **Baixados** ou **Parcialmente Baixados**.     **Exemplos:** |
| **Observações:** |
