---
article_id: 360058056993
category: RH - Folha de Pagamento
content_hash: 301850cd62a2186f0cca09783c4195cd9ebf2aa49c83f794b968c0c45ed9ee9e
fetched_at: '2026-06-28T22:44:15.082149+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos de empresas diferentes
type: support-article
updated_at: '2024-09-04T20:17:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058056993-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-de-empresas-diferentes
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22248958049431) Tempo aproximado para leitura: 00:03:00 min****Dúvida**Como configurar o sistema para o novo calculo múltiplos vínculos de empresa diferentes?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Visando atender ao e-Social, a rotina de múltiplos vínculos internos sofrerá algumas alterações para que fique compatível com o que o governo espera receber em se tratando de múltiplos vínculos de empresas diferentes.   
  
Necessário a inclusão do menu no sistema: via **Configurador (SIGACFG),** acessar em **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu **SIGAGPE**, conforme instruções abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097971133)  
  
Será liberado uma nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez.   
  
- **Principais Campos e Parâmetros:**

* RC\_SEQMV - Sequência de cálculo MULTV na tabela de movimento mensal;
* RD\_SEQMV - Sequência de cálculo MULTV na tabela de movimento acumulado;
* RR\_SEQMV - Sequência de cálculo MULTV na tabela de itens de férias e rescisões;
* RAZ\_CIC - CPF do Funcionário.

- **Identificadores de Cálculo necessários:**

|  |  |  |  |
| --- | --- | --- | --- |
| Id | Descrição | Tipo Cod | Tipo |
| 0236 | Base IR Férias Outos Períodos | Base Provento | Valor |
| 0237 | IR Férias Outros Períodos | Base Provento | Valor |
| 0288 | Salário Contribuição INSS Outras Empresas | Base Provento | Valor |
| 0289 | Desconto INSS Outras Empresas | Base Provento | Valor |
| 0290 | Base INSS 13º Outras Empresas | Base Provento | Valor |
| 0291 | INSS 13º Outras Empresas | Base Provento | Valor |
| 0396 | Base INSS Férias Outros Períodos | Base Provento | Valor |
| 0397 | INSS Férias Outros Períodos | Base Provento | Valor |
| 0992 | Base IR Outras Empresas | Base Provento | Valor |
| 0993 | IR Outras Empresas | Base Provento | Valor |
| 0994 | Base IR Outras Empresas 13º Salário | Base Provento | Valor |
| 0995 | IR Outras Empresas 13º Salário | Base Provento | Valor |
| 1847 | Base INSS Autônomo Outras Empresas | Base Provento | Valor |
| 1951 | Deduções modelo completo IR Folha no período anterior | Base Provento | Valor |

**OBS.:** Para que o cálculo no novo formato seja executado, deverá ser ativado o **mnemônico P\_MULTV**, além de aplicar o pacote com o diferencial de dicionário onde serão criados alguns campos. A partir do momento que o pacote for aplicado, e o mnemônico ativado, a fórmula S\_MULTV(), existente no roteiro de cálculo, deixará de ser executada.

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)

RH - Linha Protheus - GPE - Como configurar o cálculo de múltiplos vínculos na versão 12: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027693112?source=search>
