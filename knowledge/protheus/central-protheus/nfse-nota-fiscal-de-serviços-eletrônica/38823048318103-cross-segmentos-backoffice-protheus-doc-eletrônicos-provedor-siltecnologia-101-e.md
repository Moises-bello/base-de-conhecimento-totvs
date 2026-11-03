---
article_id: 38823048318103
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1dcb152074c282ab0435eb4dd47a0e4a1588f60ec7132ba39deddc7a8bcb56d1
fetched_at: '2026-06-28T22:39:58.687962+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Provedor SilTecnologia
  1.01 : Erros mapeados no novo layout da NFSE'
type: support-article
updated_at: '2026-04-15T23:32:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38823048318103-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Provedor-SilTecnologia-1-01-Erros-mapeados-no-novo-layout-da-NFSE
---

**Dúvida**  
Desde 01/01/2026 entrou em produção um novo layout da NFSE para as prefeituras.

Bauru / Vila Velha / Itapevi

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

**1.**Para municípios aderentes ao Provedor Provedor SilTecnologia 1.01, realize as atualizações abaixo no ambiente:  
  
**PROTHEUS**

**PROTHEUS**  
Expedição continua Protheus com os fontes atualizados até o dia 26/02:  
12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>   
12.1.2510: <https://suporte.totvs.com/portal/p/10098/download?e=1224039>

NFSEXMLENV 14/04/2026:

12.1.2410:<https://r.totvs.io/p/1246515> (Aplicar pacote PTM e compilar no RPO do Protheus).  
12.1.2510:<https://r.totvs.io/p/1246512> (Aplicar pacote PTM e compilar no RPO do Protheus).

Precisamos que os fontes sejam atualizados conforme indicado nesta interação. A expedição continua: -> NFSEXMLENV.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39141907844119)

**TSS**

Pacote pontual disponibilizado 06/04/2026

- [12.1.2410](https://r.totvs.io/p/1245321)| [12.1.2510](https://r.totvs.io/p/1245318)

-[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)

**Importante** :

Dentro desse pacote, há alguns arquivos importantes:

 -xsd deve ser informado na pasta SCHEMAS

-tssnewnfse.json na pasta SYSTEM

 Após isso, é necessário reiniciar os serviços do TSS

**2.**Depois derealizadas as atualizações, ao acessar a rotina FISA022 deverá informar as opções relacionadas ao modelo Prefeitura.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38823048314135):

Após isso, deverá alterar a versão de layout para **'1.01'**, tanto em **homologação**quanto **produção**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38823048314263)

Abaixo listamos todos os erros mapeados até o momento para a transmissão da nota:

**O campo Série RPS é estritamente numérico.**

Após a migração para o layout nacional, é necessário ajustar a numeração da série conforme o padrão exigido. Enquanto as prefeituras aceitavam séries como NFSE, RPS, entre outras, o layout nacional permite apenas caracteres numéricos.

 Configurações importantes:

* Série: deve ser numérica, entre 1 e 999.
* Espécie: deve ser exatamente 'RPS', seguindo o mesmo padrão utilizado para modelos de prefeitura. Para mais detalhes, consulte a documentação: [Documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000308521-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-COMO-CRIAR-UMA-ESPECIE-PARA-NFSE)

**O endereço de e-mail do prestador e invalido.**

 A rejeição acontece porque está utilizando um e-mail inválido no parâmetro MV\_EMAILPT, ou há algum conteúdo inválido nele, por exemplo, .T.

**O Telefone do Prestador é inválido. Atualize os dados de contato do Prestador antes de prosseguir com a emissão.**

A rejeição ocorre porque o número de telefone informado no cadastro da Filial  está incorreto, o campo não pode ter espaço, nem caracteres como parênteses e traço.

Exemplo válido: 01123456789 

**Código de Tributação Nacional informado e invalido para o município. Código:**

Essa rejeição  ocorre quando a TAG cTribNac não é gerada ou seu conteúdo está incorreto. É necessário entrar em contato com o fiscal da empresa ou com a prefeitura para obter o código correto e ajustar o campo B1\_TRIBMUN.

Por exemplo, ao informar o código 070101 no campo B1\_TRIBMUN, os 6 dígitos serão gerados na TAG cTribNac.

<cTribNac>070101</cTribNac>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38823042860055)

**O Código de Tributação Nacional xxxxxx não pertence a lista de itens permitidas pela Prefeitura para este Prestador.**

A rejeição indica que o código de serviço prestado que você está utilizando **não está autorizado** pela prefeitura para a sua empresa ou é um código invalido.
