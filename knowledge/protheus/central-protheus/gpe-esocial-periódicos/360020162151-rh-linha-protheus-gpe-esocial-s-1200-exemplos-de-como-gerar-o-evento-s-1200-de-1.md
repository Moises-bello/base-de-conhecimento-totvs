---
article_id: 360020162151
category: GPE - eSocial - Periódicos
content_hash: 413842790db36c8c39358b24c4ed56e6999795e71000146b4976f88177ccb709
fetched_at: '2026-06-28T22:45:07.252902+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Exemplos de como gerar o evento
  S-1200 de 13º salario primeira e segunda parcela
type: support-article
updated_at: '2025-07-21T14:16:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020162151-RH-Linha-Protheus-GPE-eSocial-S-1200-Exemplos-de-como-gerar-o-evento-S-1200-de-13%C2%BA-salario-primeira-e-segunda-parcela
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19282724544023) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Exemplos de como gerar o evento S-1200 de 13º salario primeira e segunda parcela?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para acessar os exemplos de geração do calculo do 13º no evento S-1200 acesse no *link* abaixo a aba **Como Gerar** > **13º Salario**.  
  
Nessa documentação será possível encontrar exemplos conforme *Link*: [S-1200 – Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social](https://tdn.totvs.com/pages/releaseview.action?pageId=727922888)

![Entregas Legais Eventos Periodicos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19282484810263)

**S-1200 1ª Parcela Pago até 11/AAAA**  
Premissas

* Quando efetuado o cálculo da 1ª parcela do 13º salario onde o pagamento ocorre até 30/11, os valores devem ser gerados no evento S-1200 deixando o campo REF. 13 igual a NÃO, conforme exemplos abaixo.
* Conforme [Tabela 03 (Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#03) a natureza para o calculo do 13º salário 1ª parcela deve ser a **5504** (13º salário - Adiantamento) na verbas de provento/desconto utilizadas nesse calculo.
* Deve existir na base os novos IDs para separação de 13º salário 1ª parcela, consulte a documentação: [Separação de IDs 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019893271-MP-GPE-eSocial-S-1200-Para-as-informa%C3%A7%C3%B5es-do-13%C2%BA-sal%C3%A1rio-deve-ser-enviado-para-o-governo-a-1%C2%BA-parcela-com-a-natureza-de-rubrica-5504-e-a-2%C2%BA-parcela-com-a-natureza-5001-como-separar-as-verbas-de-adicionais-e-m%C3%A9dias-no-sistema?source=search)

**S-1200 2ª Parcela Pago em 12/AAAA**  
Premissas

* O calculo da primeira parcela já deve ter sido efetuado.
* Conforme [Tabela 03 (Natureza das Rubricas da Folha de Pagamento)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#03) a natureza para o calculo do 13º salário 1ª parcela deve ser a **5504** (13º salário - Adiantamento) e para 2ª parcela deve ser a **5001** (13º salário) em verbas de provento/desconto utilizadas nesse calculo

Observações Sistêmicas

* Quando efetuado o cálculo da 2ª parcela do 13º salario onde o pagamento ocorre até 20/12, os valores devem ser gerados no evento S-1200 deixando o campo **REF. 13** igual a **SIM**, no calculo da folha deve ser gerado outro S-1200 com o campo **REF. 13** igual a **NÃO**, conforme exemplos abaixo.
* O evento S-1210 não é gerado com o campo **REF. 13 SIM**, só existe um S-1210 para o mês de dezembro.
* O período de apuração (tag <perRef>) será gerada no formato **AAAA** (por exemplo: 2018).

**S-1200 2ª Parcela Pago antes de 12/AAAA**  
Premissas

* O sistema deve estar atualizado com os pacotes disponíveis em [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)
* O evento S-1210 não é gerado com o campo REF. 13 **SIM**, só existe um S-1210 para o mês de dezembro.
* Conforme [Tabela 03 (Natureza das Rubricas da Folha de Pagamento)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#03) a natureza para o calculo do 13º salário 1ª parcela deve ser a **5504** (13º salário - Adiantamento) e para 2ª parcela deve ser a **5001** (13º salário) em verbas de provento/desconto utilizadas nesse calculo.
* Deve no cadastro uma verba de desconto vinculada ao id **1655** (13º integral pago antes de dezembro) com incidência para FGTS.

Observações Sistêmicas:  
**13º Salario 2ª Parcela Calculo total em 11/AAAA**

* + Em novembro ao gerar a rotina eventos periódicos o campo Ref. 13 deve ficar com **NÃO**. Os valores de calculo do 13º 1ª parcela são gerados no S-1200 junto com o calculo da folha;
  + Em dezembro será necessário gerar 2 eventos S-1200 mesmo que o calculo total foi efetuado em novembro, um com o campo **Ref. 13** deve ficar com **SIM** para gerar no TAF os valores da folha de 13º salario, e outro com S-1200 com o campo **Ref. 13** com **NÃO** para gerar o valor da folha de dezembro;
  + Deve ser gerado apenas 1 evento S-1210 que contém que vai conter as informações da folha e 13º salario.
  + O evento S-1210 de dezembro referente ao roteiro 132 será gerado com valor zerado, devido a inclusão do desconto do adiantamento e as rubricas de IRRF e/ou pensão alimentícia serão geradas normalmente.
  + O período de apuração (tag <perRef>) será gerada no formato AAAA (por exemplo: 2018).

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
