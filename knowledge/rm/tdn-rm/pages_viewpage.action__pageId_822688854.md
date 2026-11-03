---
content_hash: ca6380938bbfa7bd8879d8b70ef41252c8770c20b5de5270989813fc3af802b8
fetched_at: '2026-06-29T00:11:46.535525+00:00'
page_id: '822688854'
product: rm
source: tdn-rm
title: trib/tribMun
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688854
version: 19
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **trib** | **DPS/infDPS/valores** | **Sim** | **Grupo** | **Grupo de informações dos tributos do serviço prestado.** |
| **tribMun** | **DPS/infDPS/valores/trib** | **Sim** | **Grupo** | **Grupo de informações relacionados ao ISSQN** |
| tribISSQN | DPS/infDPS/valores/trib/tribMun | Sim | Cadastro da Filial | Anexo | Dados Fiscais | Tributos | Regime de ISS  DFILIAL.REGIMEISS | Tributação do ISSQN sobre o serviço prestado.   * 1 - Operação Tributável: será gerado para os seguintes valores do campo "Regime ISS": Construção Civil, Sociedade Profissional, Cooperativa, Estimativa, e Não se aplica; * 2 - Imunidade: será gerado para o valor Imune; * 3 - Exportação de Serviço: será gerado para o valor Exportação de Serviço; * 4 - Não Incidência: será gerado para o valor Isenta ISSQN. |
| cPaisResult | DPS/infDPS/valores/trib/tribMun | Não | DPAIS.CODPAIS | Gerado com o código do país do estado informado na aba "Integrações, Fiscal" do movimento.  É necessário que o município e o estado informados tenham uma classificação cadastrada.  Esta tag não é gerada para estados nacionais. |
| tpImunidade | DPS/infDPS/valores/trib/tribMun | Não | DFILIAL.TIPOIMUNIDADE | Gerado quando o Regime Tributário da filial for igual a Imune e o tipo de imunidade (disponível em Filial > Anexos > Dados Fiscais, conforme [documentação](https://tdn.totvs.com/display/public/LRM/Dados+Fiscais#1-1563551098)) estiver preenchido.   * 0 - Imunidade (tipo não informado na nota de origem); * 1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a); * 2 - Templos de qualquer culto (CF88, Art 150, VI, b); * 3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c); * 4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d); * 5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e); |
| pAliq | DPS/infDPS/valores/trib/tribMun | Não | Tributos dos Itens ou do movimento  TTRBMOV.ALIQUOTA | Valor da alíquota do serviço prestado relativo ao município de incidência do ISSQN.   * Se o município de incidência pertence ao Sistema Nacional NFS-e a alíquota estará parametrizada e, portanto, será fornecida pelo sistema. * Se o município de incidência não pertence ao Sistema Nacional NFS-e a alíquota não estará parametrizada e, por isso, deverá ser fornecida pelo emitente.     Para detalhes sobre a regra de remoção da tag de acordo com a data da integração do município ao Layout Nacional, acesse: |
| tpRetISSQN | DPS/infDPS/valores/trib/tribMun | Não | Tributos dos Itens ou do movimento  TTRBMOV.TIPORECOLHIMENTO | Tipo de retenção do ISSQN.   * 1 - Não Retido: será gerado para os seguintes valores do campo "Tipo Recolhimento": Nenhum, Isento e Imune, Devido e Depósito Juízo; * 2 - Retido pelo Tomador: será gerado para os valores Retido Fonte, Retido Fonte Deduzido. * 3 - Retido pelo Intermediário: Não é gerado |
