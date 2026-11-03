---
article_id: 17509366898199
category: RH - Sindicais
content_hash: 4d1907e5332b05a186fd76e891159e3d2ff95ce4a5a12195a43aceb995ddf9d4
fetched_at: '2026-06-28T22:43:10.909444+00:00'
product: protheus
section_id: 360011997333
source: central-protheus
title: 'RH - Linha Protheus - GPE - Contribuição Sindical do Produtor Rural '
type: support-article
updated_at: '2025-06-06T18:56:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17509366898199-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-Sindical-do-Produtor-Rural
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17509355348375) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como realizar o desconto da Contribuição Sindical do Produtor Rural?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Em virtude da necessidade de adequação do cálculo da contribuição sindical para produtores rurais (conforme disposto no Decreto-Lei nº 1.166/1971 , art. 4º , § 2º), onde é utilizado o salário mínimo como base da referida contribuição, foi necessária a criação de uma nova tabela para que o usuário possa informar os dados para esse cálculo.

Obs.: Utilizamos como embasamento a consultoria jurídica disponível em: [http://tdn.totvs.com/x/LgFRCg](https://tdn.totvs.com/x/LgFRCg)

Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Na rotina de "Manutenção de Tabelas", localizada no menu "Atualizações-Definições de Cálculo", está disponível a nova tabela S127 - CONTRIBUICAO SINDICAL RURAL, para preenchimentos dos seguintes campos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17509135306903)

- Filial: código da filial para filtro do cálculo (campo não obrigatório);  
- Ano Contribuição: ano da competência da folha em que será gerado o desconto da contribuição (campo obrigatório);  
- Maior Qtde. Func.: quantidade de funcionários que trabalharam na área na época de maior serviço (campo obrigatório);  
- Funcionários Ativos: quantidade de funcionários que estiverem trabalhando em março do Ano Contribuição (campo obrigatório);  
- Sindicato: código do sindicato para filtro do cálculo (campo não obrigatório);  
- Centro de Custo: código do centro de custo para filtro do cálculo (campo não obrigatório).

2. Na rotina de "Manutenção de Tabelas", localizada no meu "Atualizações - Definições de Cálculo" deve existir o cadastro do salario Mínimo do Ano Vigente do Calculo ;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17509182250263)

Após o preenchimento da tabela, no mês em que é devido o cálculo da contribuição sindical, o sistema gerará o desconto obedecendo ao critério especificado na lei:  
**(SALÁRIO MÍNIMO) / (30 DIAS) X (MAIOR QTDE. FUNC.) / (FUNCIONARIOS ATIVOS)**

**INFORMAÇÕES A DESTACAR**

1)  Somente os funcionários que possuem em seus cadastros o campo "Tipo Admiss." (RA\_TIPOADM) com os códigos 2A, 2B ou 2C (que identificam os trabalhadores rurais), estão sujeitos ao cálculo determinado nesse boletim.

2) A base de cálculo para todos os funcionários é a divisão do salário mínimo por 30, independentemente da parametrização de dias do mês definida nos demais cálculos da folha.

**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=330140503>

[RH - Linha Protheus - GPE - Contribuição Sindical, Contribuição Assistencial e Contribuição Confederativa na RAIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024749732-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-Sindical-Contribui%C3%A7%C3%A3o-Assistencial-e-Contribui%C3%A7%C3%A3o-Confederativa-na-RAIS?source=search)  
[RH - Linha Protheus - GPE - Contribuição sindical mês de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056721194-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-sindical-m%C3%AAs-de-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Como definir se será calculada as contribuições confederativa, assistencial e mensalidade sindical para empregados afastados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025817211-RH-Linha-Protheus-GPE-Como-definir-se-ser%C3%A1-calculada-as-contribui%C3%A7%C3%B5es-confederativa-assistencial-e-mensalidade-sindical-para-empregados-afastados?source=search)  
[RH - Linha Protheus - GPE - Como configurar as verbas de contribuição sindical para funcionários e profissionais liberais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024693292-RH-Linha-Protheus-GPE-Como-configurar-as-verbas-de-contribui%C3%A7%C3%A3o-sindical-para-funcion%C3%A1rios-e-profissionais-liberais?source=search)  
[RH - Linha Protheus - GPE - Contribuição assistencial para colaborador Horista Jornada Variável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004974782-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-assistencial-para-colaborador-Horista-Jornada-Vari%C3%A1vel-?source=search)
