---
article_id: 40719790920727
category: Faturamento - Cadastros
content_hash: 9cec7c6ded3067b8474384ab7c00fa91c71f6a33ebc3601f75ff14b695dd8de0
fetched_at: '2026-06-28T22:38:36.740049+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - CNPJ Alfanumérico no Faturamento
type: support-article
updated_at: '2026-06-12T20:41:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40719790920727-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-CNPJ-Alfanum%C3%A9rico-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40719790906135) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Quais foram as mudanças sobre o CNPJ Alfanumérico no Faturamento?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
No Faturamento, a tratativa dos campos de CNPJ para formato alfanumérico foi implementada por meio do pacote de expedição contínua, com alteração das máscaras e validações dos campos de CNPJ:

| Campo | Picture Anterior | Nova Picture | X3\_VALID |
| --- | --- | --- | --- |
| **A1U\_CGC** | **@R 99.999.999/9999-99** | **@!R NN.NNN.NNN/NNNN-99** | **Já possui validação padrão.** |
| AD0\_CNPJ | @1 | @!R NN.NNN.NNN/NNNN-99 | Vazio() .Or. CGC(M->AD0\_CNPJ) |
| ADL\_CGC |  | @!R NN.NNN.NNN/NNNN-99 | Vazio() .Or. CGC(M->ADL\_CGC) |
| A4\_CGC | @R 99.999.999/9999-99 | @!R NN.NNN.NNN/NNNN-99 | Já possui validação padrão. |
| C5\_CGCINT | @! | @!R NN.NNN.NNN/NNNN-99 | Vazio() .Or. CGC(M->C5\_CGCINT) |
| D9\_CNPJ | @! | @!R NN.NNN.NNN/NNNN-99 | Vazio() .Or. CGC(M->D9\_CNPJ) |
| F2\_CGCCLI | @R 99.999.999/9999-99 | @!R NN.NNN.NNN/NNNN-99 | Vazio() .Or. CGC(M->F2\_CGCCLI) |
| A1\_CGC | @R 99.999.999/9999-99 | @!R NN.NNN.NNN/NNNN-99 | Já possui validação padrão. |

Abaixo, segue passo a passo para a aplicação do dicionário e execução do UPDDISTR, necessários para a adequação do formato dos campos CGC em seu ambiente.

---

1 - Aplique o pacote de 'Expedição Contínua'conforme sua release: [Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)

Exemplo:   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40719818290711)**  
2 - Aplique o dicionário contido na pasta "sdf": **Abra a pasta SDF > Abra a pasta "bra" > Copie todas as pastas e cole (substituindo) dentro da pasta "" do ambiente Protheus "protheus > protheus\_data > systemload".**  
  
3 - Rode o UPDDISTR para compatibilizar os dicionários e as tabelas necessárias.

Se o ambiente for Cloud, recomendamos seguir o processo presente na documentação do time: [**CLOUD - MP - Aplicar Pacote (Patch)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024948533-CLOUD-MP-Aplicar-Pacote-Patch). Se surgir alguma dúvida/impeditivo sobre o processo documentado, recomendamos abrir um chat/ticket com a equipe Cloud para auxiliarem.

---

**Observações**

* O Faturamento irá atuar apenas em alguns Cadastros que utilizarão o novo formato de CNPJ, especificamente sobre os campos informados acima.
* Caso tenha alguma dúvida/impeditivo referente ao processo da transmissão da nota, recomendamos abrir um chat/ticket com a equipe Protheus SPED para auxiliarem.
* O pacote de expedição contínua engloba os módulos: (ATF, COM, CRM, CTB, EST, FAT, FIN, FIS, PCO)

**Exemplo Cadastro de Clientes:**

**Receita disponibilizou o Simulador CNPJ Alfanumérico.**

<https://servicos.receitafederal.gov.br/servico/cnpj-alfa/simular>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41186635504791)

**Saiba mais**

* [**https://espacolegislacao.totvs.com/cnpj-alfanumerico/?utm\_term=&hsa\_grp=&hsa\_ad=&hsa\_tgt=&hsa\_kw=&hsa\_mt=&gad\_campaignid=23507109535#transicao**](https://espacolegislacao.totvs.com/cnpj-alfanumerico/?utm_term=&hsa_grp=&hsa_ad=&hsa_tgt=&hsa_kw=&hsa_mt=&gad_campaignid=23507109535#transicao)
* [**DT Débito Técnico - Alteração da picture de campos de CNPJ - FAT**](https://tdn.totvs.com/pages/viewpage.action?pageId=908682529).
