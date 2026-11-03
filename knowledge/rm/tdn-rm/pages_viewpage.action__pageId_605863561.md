---
content_hash: c7d2512f965fb47fa8ee4285d768dba45e505c67cebbff1dd2a23da00a85ada1
fetched_at: '2026-06-29T00:10:58.341922+00:00'
page_id: '605863561'
product: rm
source: tdn-rm
title: Alterações S-1010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=605863561
version: 13
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1010 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {ideEmpregador} Campo {nrInsc} | Alterado tamanho: 15  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Tamanho: 14  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Neste caso, deve ser informada apenas a raiz/base (8 posições), exceto se natureza jurídica do declarante for igual a ([1015, 1040, 1074, 1104, 1139, 1163, 1198, 1252, 1287, 1317, 1341]), situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Se {tpInsc} for igual a [2], deve ser um CPF válido. |
| Grupos {dadosRubrica}: Campo {codIncIRRF} tamanho alterado | 2 | 4 |
| Grupos {dadosRubrica}: Campo {codIncFGTS} incluído valores. | Código de incidência da rubrica para o FGTS: 00 - Não é Base de Cálculo do FGTS; 11 - Base de Cálculo do FGTS; 12 - Base de Cálculo do FGTS 13° salário; 21 - Base de Cálculo do FGTS Rescisório (aviso prévio); 91 - Incidência suspensa em decorrência de decisão judicial. Validação: No caso de preenchimento com o código 91, é necessária a existência de registro complementar com informações relativas ao processo. Valores Válidos: 00, 11, 12, 21, 91. | Código de incidência da rubrica para o Fundo de Garantia do Tempo de Serviço - FGTS. Valores válidos: 00 - Não é base de cálculo do FGTS 11 - Base de cálculo do FGTS mensal 12 - Base de cálculo do FGTS 13° salário 21 - Base de cálculo do FGTS aviso prévio indenizado 91 - Incidência suspensa em decorrência de decisão judicial - FGTS mensal 92 - Incidência suspensa em decorrência de decisão judicial - FGTS 13º salário 93 - Incidência suspensa em decorrência de decisão judicial - FGTS aviso prévio indenizado Validação: Para utilização de código [91, 92, 93], é necessária a existência de grupo com informações relativas ao processo. |
| Grupos {dadosRubrica}: Campo {codIncSIND } excluído. |  |  |
| Grupo {ideProcessoIRRF} alterada condição | O (se {codIncIRRF} do registro superior for igual a [9x]) N (Nos demais casos). | O (se codIncIRRF = [9X] ou [9XXX]); N (nos demais casos). |
| Grupo{ideProcessoSIND} e campo {nrProc} excluído |  |  |
| Grupo{ideProcessoCP}: campo {nrProc} alterada condição. | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1]. Validação: Deve ser um número de processo válido e existente na Tabela de Processos (S-1070). 57 | Informar um número de processo cadastrado através do evento S-1070, cujo indMatProc seja igual a [1]. Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos (S1070), com indMatProc = [1]. |
| Grupo{ideProcessoIRRF}: campo {nrProc} alterada condição. | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1]. Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070). | Informar um número de processo judicial cadastrado através do evento S-1070, cujo indMatProc seja igual a [1]. Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070), com indMatProc = [1]. |
| Grupo{ideProcessoFGTS}: campo {nrProc} alterada condição. | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1, 7]. Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070). | Informar um número de processo judicial cadastrado através do evento S-1070, cujo indMatProc seja igual a [1, 7]. Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070), com indMatProc = [1, 7]. |

Foram realizados ajustes em alguns campos no cadastro de eventos e validações na geração do XML.

Acesse **RH | Folha de Pagamento | Administração de Pessoal | Eventos | Aba Inc. Proventos**

Na parte de Incidência(s) suspensa(s) em decorrência de decisão judicial no campo INSS, foram substituídos os checkbox's por combobox com as opções.

**OBSERVAÇÃO:**

Caso alguns checkbox's de suspensão de incidência de INSS esteja marcado na versão anterior, ao rodar o atualizador o mesmo será ajustado para o combobox correto.

**Exemplo:** flag selecionada **Incidência INSS**, ao rodar o atualizador o sistema ira preencher o combobox correspondente ao **91 - Mensal.**

Na parte de Incidência(s) suspensa(s) em decorrência de decisão judicial no campo IRRF, foram substituídos os checkbox's por combobox com as opções.

**Observação:**Caso alguns checkbox's de suspensão de incidência de IRRF esteja marcado na versão anterior, ao rodar o atualizador o mesmo será ajustado para o combobox correto. Exemplo: flag selecionada **Incidência IRRF**, ao rodar o atualizador o sistema ira preencher o combobox correspondente ao **9011 - Remuneração** **mensal.**

Na parte de Incidência(s) suspensa(s) em decorrência de decisão judicial no campo incidência de FGTS, foi substituído o checkbox por combobox com as opções.

**Observação:**Caso alguns checkbox's de suspensão de incidência de FGTS esteja marcado na versão anterior, ao rodar o atualizador o mesmo será ajustado para o combobox correto. Exemplo: flag selecionada **Incidência FGTS**, ao rodar o atualizador o sistema ira preencher o combobox correspondente ao **FGTS mensal.**

Ao gerar o xml no novo leiaute (S-1.0)  será apresentado erro para a tag codIncIRRF com os valores não existentes no leiaute e que deverão ocorrer DE/PARA manual. Exemplos de alterações manuais :  Código 01- Rendimento não tributável em função de acordos internacionais de bitributação // Código 00 - Rendimento não tributável

Criação do campo "Compõe Teto Remuneratório (art. 37, XI, da CF/1988)" para preencher a tag <tetoRemun>, gerada quando a natureza jurídica do declarante for Administração Pública (grupo [1]).

Criação do campo "Contribuições RPPS/Regime Militar" para preencher a tag <codIncCPRP>. Observação campo liberado nas versões: 12.1.31.248, 12.1.32.188, 12.1.33.115 e superiores.
