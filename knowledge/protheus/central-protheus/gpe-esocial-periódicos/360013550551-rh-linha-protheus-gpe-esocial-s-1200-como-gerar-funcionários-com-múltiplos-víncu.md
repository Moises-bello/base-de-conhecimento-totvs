---
article_id: 360013550551
category: GPE - eSocial - Periódicos
content_hash: 9ed6def978f82feb1048712a58dd27390c575ae559d582b9c18e1772ebf01203
fetched_at: '2026-06-28T22:45:07.204826+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar funcionários com
  múltiplos vínculos no evento S-1200
type: support-article
updated_at: '2026-02-19T11:34:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013550551-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-no-evento-S-1200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27049565770903) Tempo aproximado para leitura: **00:07:00 min  
  
Dúvida**Como gerar funcionários com múltiplos vínculos no evento S-1200?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para geração do calculo de folha dos trabalhadores com os múltiplos vínculos no evento S-1200 / S-1210 deve ser analisado os cenários abaixo:  
  
**Premissas:**  
Acessar a rotina **GPEA300** no caminho: *Atualizações > Definições de Calculo > Mnemônicos* e verificar os seguintes mnemônicos:

**P\_ESOCMV**:  Deve ficar com .T. em todas as filiais  
**P\_MULTV**: Deve ficar com .T. em todas as filiais

**Possíveis cenários de cálculo:**

1. Múltiplos vínculos empresas de CNPJ RAIZ diferente, onde as empresas/filiais **estão dentro do mesmo grupo no Protheus.**
2. Múltiplos vínculos empresas de CNPJ RAIZ diferente, onde as empresas/filiais **não estão dentro do mesmo grupo no Protheus**, ou o outro vinculo **não está no Protheus.**2.1. Múltiplos vínculos empresas de CNPJ RAIZ diferente**(valor fixo).**
3. Múltiplos vínculos empresas de CNPJ RAIZ iguais, onde as empresas/filiais **estão dentro do mesmo grupo no Protheus.**

**Detalhes de cada cenário:**  
**1.** Múltiplos vínculos empresas de CNPJ RAIZ diferente, onde as empresas/filiais **estão dentro do mesmo grupo no Protheus.**

Após o calculo da folha executar por ultimo o calculo do Múltiplo Vinculo na rotina **GPEM930** (caminho *Atualizações > Miscelânea > Múltiplos Vínculos*). Nessa rotina deve ser marcado todos os vínculos e na parte inferior é possível definir a ordem do calculo conforme exemplo da imagem:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402313770391)  
  
Após realizar o calculo, o sistema alimenta de forma automática a rotina **GPEA924** (visualização dados de múltiplos vínculos) com o indicativo de múltiplo vinculo na *tag* **IndMV** e os dados do outros empregadores, conforme imagem de exemplo abaixo. E essa mesma informação será gerada no **S-1200** do trabalhador.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402818283543)  
  
Caso necessite visualizar ou fazer manutenção na rotina **GPEA924** (visualização dados de múltiplos vínculos) acesse o artigo: **[S-1200 - Para que serve e como realizar ajustes na rotina GPEA924 para Múltiplos Vínculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029145033)**  
  
**Importante**  
O governo estabelece regras sobre o calculo e qual vinculo deve enviar a informação de outros empregadores. Por isso orientamos que veja as regras do eSocial no item **5 - Múltiplos Vínculos**, do [MOS S-1.2 do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf).  
  
**2.** Múltiplos vínculos empresas de CNPJ RAIZ diferente, onde as empresas/filiais **não estão dentro do mesmo grupo no Protheus**, ou o outro vinculo **não está no Protheus.**Ao realizar o **lançamento** manual para um funcionário na rotina **GPEA090** (caminho*Atualizações > Lançamentos > Por Funcionário*), quando informado as verbas com a Base e Desconto de INSS Outras Empresas  vinculado aos **ID's de calculo padrão** (é possível ver os IDs no final do tópico), será aberta uma tela, onde o usuário informará os Detalhes de Múltiplos Vínculos.   
  
Deverá ser informado o CNPJ (lembrando que os 8 primeiros dígitos não podem pertencer a empresa que o funcionário está cadastrado), Indicador de recolhimento (**IndMV)**, Categoria do trabalhador na outra empresa e Valor do rendimento na outra empresa.  
  
Exemplo:  
Lançando as verba de Base e Desconto de INSS Outras Empresas vinculado aos ID's de calculo  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403014268567)  
  
Após clicar em salvar o sistema vai demonstrar a seguinte tela para preenchimento dos campos em destaque.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403014318871)  
  
Após confirmar a inclusão a o registro fica gravado na rotina **GPEA924** (visualização dados de múltiplos vínculos), e essa mesma informação será gerada no **S-1200** do trabalhador. Caso necessite visualizar ou fazer manutenção na rotina **GPEA924** (visualização dados de múltiplos vínculos) acesse o artigo: **[S-1200 - Para que serve e como realizar ajustes na rotina GPEA924 para Múltiplos Vínculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029145033)**  
  
Abaixo deixo a imagem de dos IDs disponíveis no sistema para múltiplos vínculos.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402313821079)  
  
**Importante**  
O governo estabelece regras sobre o calculo e qual vinculo deve enviar a informação de outros empregadores. Por isso orientamos que veja as regras do eSocial no item **5 - Múltiplos Vínculos**, do [MOS S-1.2 do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf).  
  
**2.1.** Múltiplos vínculos empresas de CNPJ RAIZ diferente **(valor fixo).**Caso o valor da Base INSS e Desconto INSS outras empresas, seja o mesmo todos os meses o usuário tem a opção de utilizar a rotinaGPEA550 (Caminho: *Atualizações > Lançamentos > Lançamentos Fixos*). Após informar as verbas com a Base e Desconto de INSS Outras Empresas vinculado aos **ID's de calculo padrão** (é possível ver os IDs no final do tópico), será aberta uma tela, onde o usuário informará os Detalhes de Múltiplos Vínculos.   
  
Deverá ser informado o CNPJ (lembrando que os 8 primeiros dígitos não podem pertencer a empresa que o funcionário está cadastrado), Indicador de recolhimento, Categoria do trabalhador na outra empresa e Valor do rendimento na outra empresa.

Exemplo:

Lançando as verba de Base e Desconto de INSS Outras Empresas vinculado aos ID's de calculo  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403021039255)  
  
Após clicar em salvar o sistema vai demonstrar a seguinte tela para preenchimento dos campos em destaque.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403014318871)  
  
Após confirmar a inclusão a o registro fica gravado na rotina **GPEA924** (visualização dados de múltiplos vínculos), e essa mesma informação será gerada no **S-1200** do trabalhador. Caso necessite visualizar ou fazer manutenção na rotina **GPEA924** (visualização dados de múltiplos vínculos) acesse o artigo: **[S-1200 - Para que serve e como realizar ajustes na rotina GPEA924 para Múltiplos Vínculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029145033)**  
  
Abaixo deixo a imagem de dos IDs disponíveis no sistema para múltiplos vínculos.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402313821079)  
  
**Importante**  
O governo estabelece regras sobre o calculo e qual vinculo deve enviar a informação de outros empregadores. Por isso orientamos que veja as regras do eSocial no item **5 - Múltiplos Vínculos**, do [MOS S-1.2 do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf).  
  
**3.** Múltiplos vínculos empresas de CNPJ RAIZ iguais, onde as empresas/filiais **estão dentro do mesmo grupo no Protheus.**

Quando os trabalhadores com mais de um vínculo estão cadastrados dentro do **SIGAGPE (mesmo empregador)** ao gerar o **S-1200** e **S-1210** será criado um único registro em cada evento com o recibo de pagamento de todos os múltiplos vínculos, separados por categoria.  
  
  
**Observação**Definição do indicativo de múltiplo vinculo (**IndMV**)  
1 = O declarante aplica a alíquota de desconto do segurado sobre a remuneração por ele informada (o percentual da alíquota será obtido considerando a remuneração total do trabalhador).

2 = O declarante aplica a alíquota de desconto do segurado sobre a diferença entre o limite máximo do salário de contribuição e a remuneração de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto.

3 = O declarante não realiza desconto do segurado, uma vez que houve desconto sobre o limite máximo de salário de contribuição em outra(s) empresa(s).  
  
[Como conferir as divergências encontradas entre o INSS apurado pelo governo e o relatório do TAF (TAFR120)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024628231)  
  
**Saiba Mais**

Para adquirir mais conhecimento acesse os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
