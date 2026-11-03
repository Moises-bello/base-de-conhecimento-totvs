---
content_hash: f65b6e6e2d5236599199a7fee5b69cfd4eb0ec779848b3898c66b6e7f4c9abf6
fetched_at: '2026-06-29T00:08:10.015512+00:00'
page_id: '240299365'
product: rm
source: tdn-rm
title: RMFIS00006_ECF Geração do Registro Y665
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240299365
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 11.82.43 e 12.1.11(patches superiores) / Layout ECF: 08/06/2016 ou superior |
| **Ocorrência:** | Parametrização e Geração do Registro Y665 - Demonstrativo das Diferenças na Adoção Inicial |
| **Ambiente:** |  |
| **Passo a passo:** | Apresenta o demonstrativo das diferenças dos saldos societário e fiscal das contas contábeis em virtude da adoção inicial das normas contábeis internacionais de acordo com o art. 175 da Instrução Normativa RFB no 1.515, de 24 de novembro de 2014. Registro obrigatório para as empresas tributadas pelo Lucro Real. - [Manual de Orientação do Leiaute da ECF](http://sped.rfb.gov.br/pasta/show/1644), Atualização: Maio de 2016, p. 817.    As contas patrimoniais (Ativo, Passivo ou PL) devem ser classificadas em relação ao Método de Controle da subconta. Após a execução do [Script do Registro Y665](ftp://ftp.rm.com.br/Clientes/TEVOMJ53113791001790/ECF/11_82/Script/), será disponibilizado na aba **Informações**, este novo campo:        **Exemplo: A) É controlada por subconta vinculada**  Esta opção significa que a empresa realiza o controle das diferenças por subcontas, ou seja, realizou os lançamentos referentes à adoção inicial, sendo assim o sistema irá calcular automaticamente o saldo societário, saldo fiscal, as diferenças e todas as informações que irão compor o registro Y665.            Deve-se associar a **Subconta** à conta principal: **Anexos | Subcontas Correlatas.**        Evidencia-se a diferença em subconta vinculada ao terreno. O lançamento deve ser feito na mesma data de adoção inicial informada nos Parâmetros da ECF.  Saldo Societário: R$120.000,00  Saldo FCONT: R$ 100.000,00  Diferença positiva a ser excluída: R$ 20.000,00        Ilustração na ECF:  |Y665|1.2.3.11.001||120000,00|D|100000,00|D|20000,00|D|A|1.2.3.11.002||||    **Exemplo: G)** **É controlada por subcontas vinculada e auxiliar.**  Mesmas informações processadas para a letra “A”, porem gerando informações das contas auxiliares.        Neste exemplo, a geração se demonstra assim:  |Y665|1.2.3.07.001||120000,00|D|100000,00|D|20000,00|D|G|1.2.3.07.002||1.2.3.07.003|| |
| **Observações:** |  |
