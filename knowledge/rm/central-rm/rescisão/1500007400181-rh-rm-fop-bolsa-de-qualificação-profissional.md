---
article_id: 1500007400181
category: Rescisão
content_hash: bbc652b3f23360d412fc5a9de8cae93b9bb9c7f3ed14f17e1de3c230a101dea5
fetched_at: '2026-06-28T22:46:55.212592+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Bolsa de Qualificação Profissional
type: support-article
updated_at: '2025-03-07T14:58:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007400181-RH-RM-FOP-Bolsa-de-Qualifica%C3%A7%C3%A3o-Profissional
---

**Dúvida**

Qual a rotina para a geração do arquivo de bolsa qualificação profissional?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir do release 12.1.27  
  
**Solução**

O Layout foi disponibilizado a partir dos patches abaixo:

* **12.1.27.302**
* **12.1.28.213**
* **12.1.29.138**
* **12.1.31.100**

A Bolsa de Qualificação Profissional é uma das modalidades do benefício Seguro-Desemprego. Ela é concedida quando o contrato de trabalho é suspenso, por dois a cinco meses, para a participação do empregado em curso ou programa de qualificação profissional oferecido pelo empregador. A suspensão contratual deve estar prevista em acordo ou convenção coletiva de trabalho e aprovada formalmente pelo trabalhador.

Excepcionalmente durante o estado de calamidade pública e da emergência de saúde pública decorrente do coronavírus (covid-19), o curso ou o programa de qualificação profissional poderá ser oferecido pelo empregador exclusivamente na modalidade não presencial e terá duração não inferior a um mês e nem superior a três meses, conforme o disposto no art. 17 da Medida Provisória nº 936, de 1º de abril de 2020.

A empresa deve transmitir, por meio do Empregador Web, dados dos trabalhadores que terão o contrato de trabalho suspenso e receberão a Bolsa de Qualificação Profissional.

Para permitir que os empregadores façam a geração desse arquivo pelo sistema RM, foi criado um novo layout de exportação para o gerador de saídas:  FOPLAY0092 Bolsa de Qualificação Profissional.TotvsGen**,** possibilitando que o usuário exporte os dados para o formato compatível para envio pelo Empregador Web.

Para a geração do layout, siga os passos no documento abaixo:

[RM - BI - Importar layout no Gerador de Saídas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012147952-RM-BI-Importar-layout-no-Gerador-de-Sa%C3%ADdas?source=search)

Selecione o local para a geração do relatório:  
  
![](https://tdn.totvs.com/download/attachments/572497620/image2020-11-17_10-51-9.png?version=1&modificationDate=1605624669737&api=v2)  
  
Após avançar, será apresentada uma tela com os seguintes parâmetros da geração:

**Obrigatórios****:**

* **Filtro do Usuário:** Neste campo é permitido fazer filtros dos funcionários que serão contemplados na geração do relatório;
* **Número do Processo:** Digite o numero do processo a ser vinculado;
* **Carga horário mínima do curso:**Cadastre o prazo do curso;
* **Percentual de cursos ou laboratórios:**Cadastre o percentual dos cursos;
* **Fórmula para cálculo do mês do último salário:**Neste campo deve informar o mês da última remuneração do funcionário. O mesmo deve ser retornado através de fórmula. Conforme o layout este campo é de preenchimento obrigatório;
* **Deseja utilizar os 4 últimos dígitos da agência bancaria?:** Quando selecionado "sim" o campo da agência bancária será preenchido com os 4 últimos algarismos.

**Observação:**

Caso o campo da conta bancaria tenha dígito verificador, deve-se utilizar o hífen para separa-lo do número da conta.

As fórmulas obrigatórias e opcionais estão presentes no documento abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=572497620>

Após preencher os campos e executar o processo, será gerado o arquivo conforme abaixo:  
  
![](https://tdn.totvs.com/download/attachments/572497620/image2020-11-17_11-18-33.png?version=1&modificationDate=1605626349027&api=v2)   
  
![](https://tdn.totvs.com/download/attachments/572497620/image2020-11-17_11-19-40.png?version=1&modificationDate=1605626416537&api=v2)  
  
O arquivo é gerado no diretório informado e com o formado .SD:  
  
![](https://tdn.totvs.com/download/attachments/572497620/image2020-11-17_11-22-53.png?version=1&modificationDate=1605626608900&api=v2)  
  
Após a geração, o arquivo pode ser validado no [Empregador Web](https://sd.mte.gov.br/sdweb/validador/validadorBolsa.html)
