---
article_id: 360017423592
category: GPE - eSocial - Periódicos
content_hash: 6b0d178e1ed42a46c731376a8a10cc04b94d214f67aa709825008a5bd7beb5c0
fetched_at: '2026-06-28T22:45:09.934729+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial/DCTFWEB - Salário-Maternidade referente
  a 13º Salário pago pela empresa e sua Compensação na DCTFWEB (LEI nº 10.710/2003)
type: support-article
updated_at: '2025-07-21T14:32:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017423592-RH-Linha-Protheus-GPE-eSocial-DCTFWEB-Sal%C3%A1rio-Maternidade-referente-a-13%C2%BA-Sal%C3%A1rio-pago-pela-empresa-e-sua-Compensa%C3%A7%C3%A3o-na-DCTFWEB-LEI-n%C2%BA-10-710-2003
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19322264032023) Tempo aproximado para leitura: 05:00 min** **Ocorrência**Salário-Maternidade referente a 13º Salário pago pela empresa e sua Compensação na **DCTFWEB** (LEI nº 10.710/2003)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Conforme o manual da DCTFWEB a compensação do salário-família e salário-maternidade deve ocorrer automaticamente, porém isso ocorre quando os eventos foram enviados de forma lógica, cronológica e preenchido corretamente (Exemplo: S-2200, S-2230, S-1200, etc).  
Fonte: <http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/DCTFWeb/>  
  
**IMPORTANTE:** A verba com o ID de cálculo 0670 (Dedução Salário Maternidade de 13° Salário na GPS) tem a função de dedução no guia da GPE emitida pelo ERP e auxilio na conferencia dos encargos, mas **não é utilizada para dedução no eSocial**.  
  
**Solução****PASSO 1:**Para o eSocial foram criados novos IDs de Cálculo que proporcionalizam o 13º Salário referente ao período de Licença Maternidade, seguem os Boletins Técnico para tal parametrização.  
  
**OBSERVAÇÃO:** A criação das verbas dos *link* abaixo devem seguir as mesmas regras de incidência da 1º e 2º parcela do 13º Salário. Veja exemplos abaixo.  
  
[RH - Linha Protheus - GPE - Separação Adicionais e Médias 2ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1434 ao 1447 e IDs 1651 a 1652)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008359545879)  
  
[RH - Linha Protheus - GPE - Separação Adicionais e Médias 1ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1639 ao 1648 e IDs 1653 a 1654)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454112)  
**PASSO 2:** Os IDs de cálculo mencionados nos links acima deverão ser configurados com a Natureza e Código de Incidência devidos nessa situação e o RET (Governo) compensará automaticamente os valores da Contribuição devida pela empresa na **DCTFWEB**.  
  
No [Leiaute vigente do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#1010_infoRubrica) **informa a tabela** que constam todos os **códigos de natureza de rubrica** previstos pelo eSocial:  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19322264033559)** **A [Tabela 03 (Natureza das Rubricas da Folha de Pagamento)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/tabelas.html#03), traz todas as Naturezas** mais comuns nessa situação:  **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9251740107415)**  
  
No [Leiaute vigente do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) é informado os **Códigos de Incidência de Contribuição Previdenciária** que devem ser informados no evento S-1010, **para os casos de licença maternidade os mais comuns são os sinalizados** abaixo: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19322264036119)  
  
**CENÁRIO 1: CASOS DE TRABALHADOR QUE ESTEVE DE LICENÇA-MATERNIDADE DURANTE UM PERÍODO NO ANO E DEPOIS FOI DEMITIDO DENTRO DO MESMO ANO:**  
Em caráter exemplificativo, um Trabalhador que ficou afastado de licença-maternidade de **01/2021** a **04/2021**, retornou ao trabalho e foi demitido em **31/08/2021**, neste caso no cálculo da rescisão deste Trabalhador ele teria direito a 8/12 relativos a **13º Salário Indenizado**, porém 4 desses avos são relativos ao período em que ele esteve de **licença-maternidade**, sendo assim deverão ser separados e informados para o **eSocial** com a incidência correta.  
  
No mesmo cenário, em valores, suponhamos que os 8/12 relativos a 13º Salário Indenizado totalizem R$ 1.000,00, neste caso as verbas deverão ser informadas na seguinte proporção:  
  
Verba de 13º Indenizado na Rescisão (ID 0114) - 4/12 = R$ 500,00   
**Natureza: 6002 - 13° salário proporcional na rescisão****In. Tr. Inss: 12 - 13o Salário**Ou seja, o governo vai entender que essa verba se trata de 13º Salário e que ela entra na base de cálculo de INSS referente ao 13º Salário.  
  
Verba de 13º Indenizado na Rescisão - Maternidade (ID 1446) - 4/12 = R$ 500,00   
**Natureza: 4051 - Salário maternidade - 13° salário   
In. Tr. Inss: 22 - Salário maternidade - 13o Salário, pago pelo Empregador;**Ou seja, o governo vai entender que essa verba se trata de 13º Salário referente ao período de Licença-Maternidade e que ela entra na base de cálculo de INSS referente ao 13º Salário, porém, devido ao código de incidência de INSS ser 22, o governo também vai entender que esse valor deverá ser abatido da contribuições previdenciária do empregador com base na LEI nº 10.710/2003, mas isso não muda em nada o desconto do Trabalhador.  
  
Verba de Dedução Salário Maternidade de 13º Salário na GPS (ID 0670) = R$ 500,00   
**Natureza: 9989 - Outros valores informativos  
In. Tr. Inss: 00 - Não é base de cálculo**Ou seja, o governo vai entender que essa verba é meramente informativa.  
  
**CENÁRIO 2 - CASOS DE 1ª PARCELA DO 13º SALÁRIO:**  
Em caráter exemplificativo, um Trabalhador que ficou afastado de licença-maternidade de **01/2021** a **04/2021**, retornou ao trabalho, neste caso no cálculo da 1ª parcela do 13º Salário deste Trabalhador ele teria direito a 12/12 relativos a **13º Salário**, porém 4 desses avos são relativos ao período em que ele esteve de **licença-maternidade**, sendo assim deverão ser separados e informados para o **eSocial** com a incidência correta.  
  
No mesmo cenário, em valores, suponhamos que os 12/12 relativos a 13º Salário Indenizado totalizem R$ 1.200,00, neste caso as verbas deverão ser informadas na seguinte proporção:  
  
Verba de 1ª Parc. 13º Sal. (ID 0022) - 8/12 = R$ 800,00   
**Natureza: 5504 - 13º salário - Adiantamento  
In. Tr. Inss: 00 - Não é base de cálculo  
In. Tr. FGTS: 12 - Base de Cálculo do FGTS 13° salário**Ou seja, o governo vai entender que essa verba se trata de ADIANTAMENTO de 13º Salário e que ela entra na base de cálculo de FGTS referente ao 13º Salário, porém não na de INSS porque isso ocorre somente na 2ª Parcela do 13º salário (Parcela Final).  
  
Verba de 1ª Parc. 13º Sal. Maternidade (ID 1434) - 4/12 = R$ 400,00   
**Natureza: 5504 - 13º salário - Adiantamento****In. Tr. Inss: 00 - Não é base de cálculo  
In. Tr. FGTS: 12 - Base de Cálculo do FGTS 13° salário**Ou seja, o governo vai entender que essa verba se trata de ADIANTAMENTO de 13º Salário referente ao período de Licença-Maternidade e que ela entra na base de cálculo de FGTS referente ao 13º Salário, porém não na de INSS porque isso ocorre somente na 2ª Parcela do 13º salário (Parcela Final).  
  
Verba de Dedução Salário Maternidade de 13º Salário na GPS (ID 0670) = R$ 400,00   
**Natureza: 9989 - Outros valores informativos  
In. Tr. Inss: 00 - Não é base de cálculo**Ou seja, o governo vai entender que essa verba é meramente informativa  
  
**CENÁRIO 3 - CASOS DE 2ª PARCELA DO 13º SALÁRIO (PARCELA FINAL):**  
Em caráter exemplificativo, um Trabalhador que ficou afastado de licença-maternidade de **01/2021** a **04/2021**, retornou ao trabalho, neste caso no cálculo da 2ª parcela do 13º Salário deste Trabalhador ele teria direito a 12/12 relativos a **13º Salário**, porém 4 desses avos são relativos ao período em que ele esteve de **licença-maternidade**, sendo assim deverão ser separados e informados para o **eSocial** com a incidência correta.  
  
No mesmo cenário, em valores, suponhamos que os 12/12 relativos a 13º Salário Indenizado totalizem R$ 1.200,00, neste caso as verbas deverão ser informadas na seguinte proporção:  
  
Verba de 2ª Parcela 13º Sal (Parcela Final)(ID 0024) - 8/12 = R$ 800,00   
**Natureza: 5001 - 13º salário  
In. Tr. Inss: 12 - 13o Salário  
In. Tr. FGTS: 12 - Base de Cálculo do FGTS 13° salário  
In. Tr. IRRF: 12 - 13o Salário**Ou seja, o governo vai entender que essa verba se trata de 13º Salário e que ela entra na base de cálculo de INSS, IRRF e FGTS referente ao 13º Salário, com relação ao FGTS o mesmo deve ser efetuado na verba de desconto da 1ª Parcela de 13º Salário (Adiantamento), assim ela deduz da base de cálculo o que já teve incidência.  
  
Verba de 2ª Parcela 13º Sal Maternidade (Parcela Final) (ID 1435) - 4/12 = R$ 400,00   
**Natureza: 4051 - Salário maternidade - 13° salário****In. Tr. Inss: 22 - Salário maternidade - 13o Salário, pago pelo Empregador  
In. Tr. FGTS: 12 - Base de Cálculo do FGTS 13° salário  
In. Tr. IRRF: 12 - 13o Salário**Ou seja, o governo vai entender que essa verba se trata de 13º Salário referente ao período de Licença-Maternidade e que ela entra na base de cálculo de INSS, IRRF e FGTS referente ao 13º Salário, com relação ao FGTS o mesmo deve ser efetuado na verba de desconto da 1ª Parcela de 13º Salário (Adiantamento), assim ela deduz da base de cálculo o que já teve incidência. Porém, devido ao código de incidência de INSS ser 22, o governo também vai entender que esse valor deverá ser abatido da contribuições previdenciária do empregador com base na LEI nº 10.710/2003, mas isso não muda em nada o desconto do Trabalhador.  
  
Verba de Dedução Salário Maternidade de 13º Salário na GPS (ID 0670) = R$ 400,00  
**Natureza: 9989 - Outros valores informativos  
In. Tr. Inss: 00 - Não é base de cálculo**Ou seja, o governo vai entender que essa verba é meramente informativa  
  
**OBSERVAÇÃO:** Vale ressaltar que esse é um cenário exemplificativo, mesmo a documentação retratando o 13º Salário a lógica se aplica para Salário Maternidade Mensal e que as incidências e naturezas deverão ser analisadas internamente por cada empresa, sempre observando os valores de médias, sobre horas, sobre valores, periculosidade e etc.  
   
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Artigos Calculo 13º Salario](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
