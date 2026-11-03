---
content_hash: 15c575810ab16c19fe5bf2aca3ae41b80c9fa10ae81c239b9a9e0be624718456
fetched_at: '2026-06-29T00:10:03.846763+00:00'
page_id: '452719163'
product: rm
source: tdn-rm
title: Atestado de Saúde Ocupacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719163
version: 10
---

**Atestado de Saúde Ocupacional**

---

   
Este processo irá criar um Atestado de Saúde Ocupacional referente à consulta selecionada. O ASO é um documento de exigência legal prevista na NR 7 (Norma Regulamentadora 7) cuja redação consta na Portaria nº 24 29/12/1994 / DOU de 30/12/1994.  
   
**Observação:**

- A nomenclatura "Mudança de Função" foi alterada para "Mudança de Riscos Ocupacionais" conforme previsto na NR 07 - PORTARIA Nº 6.734, DE 9 DE MARÇO DE 2020

- Somente consultas médicas aonde o **Tipo de Atendimento** seja igual a ***Consulta Médica Ocupacional*** são passíveis de geração do ASO.  
- Quando o  **Tipo de Atendimento** for igual a **Consulta Médica Ocupacional** e o **Tipo da Consulta para o eSocial** for **igual** a **Mudança de Riscos Ocupacionais** será apresentada a tela abaixo:

→ Se a opção "Somente os novos Riscos com informações da Função Proposta" for marcada, significa que na área "Riscos Ocupacionais Específicos Existentes" do relatório serão exibidos os riscos associados à nova Função Proposta.

→Se a opção "Riscos já presentes no funcionário trocando somente aqueles pertinentes a Função Proposta" for marcada, significa que na área "Riscos Ocupacionais Específicos Existentes" do relatório serão exibidos os riscos da Função Anterior + os riscos da nova Função Proposta.

→Se a opção "Somente os Riscos já presentes no funcionário ignorando a Função Proposta" for marcada, significa que na área "Riscos Ocupacionais Específicos Existentes" do relatório serão exibidos os riscos da Função Anterior.

- Quando o  **Tipo de Atendimento** for igual a **Consulta Médica Ocupacional** e o **Tipo da Consulta para o eSocial** for **diferente** de **Mudança de Riscos Ocupacionais** será apresentada a tela abaixo:

### 

### **Estrutura do ASO (Alterado pela Portaria nº 8, de 05 de maio de 1996):**

**Cabeçalho**

**1)** Nome completo do trabalhador, o número de registro de sua identidade e sua função; (107.048-7 / I1)  
*Origem no sistema*: Acompanhamento| Pessoas e Planejamento e Captação| Funções.  
*Origem no banco de dados:* PPESSOA.NOME, PPESSOA.CARTIDENTIDADE, PPESSOA.DTEMISSAOIDENT, PPESSOA.ORGEMISSORIDENT, PPESSOA.UFCARTIDENT, PFUNCAO.NOME.

**2)** Definição de apto ou inapto para a função específica que o trabalhador vai exercer, exerce ou exerceu; (107.052-5 / I2)  
*Origem no sistema:* Acompanhamento| Funcionários| Anexos| Segurança e Medicina| Consultas Médicas e Atendimentos Ambulatoriais.  
*Origem no banco de dados:* VCONSULTASPRONT.APTO

***Observação:***

Situação Final **Consulta Apto** -> Relatório ASO Apto

Situação Final **Consulta Inapto** -> Relatório ASO Inapto

Situação Final **Consulta Apto com Restrição** -> Relatório ASO Apto

Situação Final **Consulta Pendente** -> Relatório ASO não é gerado até que a consulta seja totalmente preenchida.

Situação Final **Consulta Agendado** -> Relatório ASO não é gerado até que a consulta seja totalmente preenchida.

Situação Final **Não Preenchida** → Relatório ASO é gerado com a situação **[SITUAÇÃO NÃO INFORMADA]**

**Riscos Ocupacionais Específicos Existentes**

**3)** Os riscos ocupacionais específicos existentes, ou a ausência deles, na atividade do empregado, conforme instruções técnicas expedidas pela Secretaria de Segurança e Saúde no Trabalho-SSST; (107.049-5 / I1)  
*Origem no sistema:* Segurança e Medicina do Trabalho| Reconhecimento e Avaliação de Risco, descrevendo o agente e seu risco.  
*Origem no banco de dados:* VPPRARISCOS.CODAGENTE, VPPRARISCOS.NOMEITEMRISCO.

**Observação**

Se o risco estiver associado ao [Perigo](https://tdn.totvs.com/display/public/LRM/Perigo), essa informação será exibida. A exibição do perigo é decorrente das alterações na NR01 conforme PORTARIA Nº 6.730, DE 9 DE MARÇO DE 2020. 

**Procedimentos Médicos Realizados**

**4)** Indicação dos procedimentos médicos a que foi submetido o trabalhador, incluindo os exames complementares e a data em que foram realizados; (107.050-9 / I1)  
*Origem no sistema:* Descrição do tipo de consulta em Acompanhamento| Funcionários| Anexos| Segurança e Medicina| Consultas Médicas e Atendimentos Ambulatoriais.  
*Origem no banco de dados:* VTIPOCONSULTA.DESCRICAO

**Exames Complementares**  
Data do exame e a descrição do exame informado no cadastro do exame.  
*Origem no sistema:* Acompanhamento| Funcionários| Anexos| Segurança e Medicina| Consultas Médicas e Atendimentos Ambulatoriais| Anexos| Exames realizados.  
*Origem no banco de dados:*  VEXAMESPRONT.DATAEXAME, VEXAMES.NOMEEXAME.  
***Observação*:** Caso o exame tenha alguma observação a mesma será inserida entre parênteses após o nome do exame realizado (VEXAMESPRONT.OBSERVACAO).

**Observação:**  
O "Exame Toxicológico" informado nos parâmetros do sistema não são considerados neste relatório, de acordo com instruções do Ministério do Trabalho.

**Coordenador(a) do PCMSO**

**5)** O nome do coordenador do PCMSO com o respectivo Registro Conselho Classe; (107.051-7 / I2)  
*Origem no sistema:* Segurança e Medicina do Trabalho| PCMSO| Responsável pela Monitoração Biológica.  
 ***Observação:*** A data da consulta e exames do funcionário deve coincidir com a data início e data fim do Responsável pela Monitoração Biológica.  
*Origem no banco de dados:* PPESSOA.NOME, VRESPMONBIOLOGICA.REGCONSELHOCLASSE.

**6)** Campo observação presente no cadastro da consulta.  
*Origem no sistema:* Acompanhamento| Funcionários| Anexos| Segurança e Medicina| Consultas Médicas e Atendimentos Ambulatoriais.  
*Origem no banco de dados:* VCONSULTASPRONT.OBSERVACAO

**Médico de Trabalho**

**7)** Nome do médico encarregado do exame e endereço ou forma de contato; (107.053-3 / I2)  
*Origem no sistema:* Segurança e Medicina do Trabalho| Cadastros| Profissional de Saúde e Acompanhamento| Funcionários| Anexos| Segurança e Medicina| Consultas Médicas e Atendimentos Ambulatoriais,

campo Código do Médico.  Forma de Contato e/ou Endereço: Segurança e Medicina do Trabalho| Cadastros| Pessoas | Anexos | Endereço Complementar.  
***Observação:*** O Endereço deverá ser do tipo Comercial e   
*Origem no banco de dados:*  VPROFISSIONALSAUDE.NOMEPROFISSIONAL, VPROFISSIONALSAUDE.CODORGAOCLASSE, VPROFISSIONALSAUDE.NUMEROREGISTRO, VPROFISSIONALSAUDE.CODUFREGISTRO.GENDERECO.RUA, GENDERECO.NUMERO, GENDERECO.COMPLEMENTO, GENDERECO.BAIRRO, GENDERECO.CIDADE, GENDERECO.ESTADO, GENDERECO.CEP, GENDERECO.DDD, GENDERECO.TELEFONE, GENDERECO.EMAIL

**Observações**

- Para executar este processo é necessário selecionar somente um registro;

- Possibilidade de exibir os dados da coligada no cabeçalho do relatório;

- Possibilidade de exibir número e total de páginas no rodapé do relatório;

- Se o parâmetro "Considerar dados da filial do funcionário para o endereço" estiver marcado, ele considera a Cidade(Município) informada no endereço da Filial para informar no relatório ASO. Caso contrário, ele considera a Cidade (Município) informada no endereço da Coligada.  
   
 

|  |  |
| --- | --- |
|  | Veja Também |

---

[Conteúdo completo da NR7](http://sislex.previdencia.gov.br/paginas/05/mtb/7.htm)
