---
article_id: 16419065822999
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: fa5cd333150207f608ff94e029abb2cfa39fdd691cbd43e911131813c56dfdb3
fetched_at: '2026-06-28T22:38:52.739416+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP FECHTO Não pode
  ser digitado movimento com data anterior a última data de fechamento (virada de
  saldos)
type: support-article
updated_at: '2025-10-06T19:22:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16419065822999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-FECHTO-N%C3%A3o-pode-ser-digitado-movimento-com-data-anterior-a-%C3%BAltima-data-de-fechamento-virada-de-saldos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16419076312727) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao tentar realizar algum processo no sistema que envolve movimentação de produto, exibe o Help:

AJUDA:FECHTO Não pode ser digitado movimento com data anterior a última data de fechamento (virada de saldos)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16416184674711)

Em integração, como por exemplo no PIMS:

![](https://totvssuporte.zendesk.com/attachments/token/ydumHpp0i7PfZB9ifY8ZgAQ62/?name=inline-1727738267.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Esse help é exibido pois, realmente, não é permitido realizar movimentações de um produto quando a origem dessa movimentação é anterior á data de fechamento do Estoque. Essa mensagem indica que está tentando movimentar / estornar / modificar registros que já foram "isolados" pelo processo de fechamento do Estoque. Ou seja, tais registros não poderiam, de fato, serem modificados pois já houve fechamento de Estoque do período, e haveria uma quebra de integridade do fechamento.

**Um causa de erro de processo, é estar posicionado no "documento incorreto",** por exemplo na PRE-NOTA (MATA140), valide se voce não tem algum filtro que esteja apontando para um documento que de fato esta fora do periodo.

**Solução** **1)** Verifique a data do último Fechamento do Estoque que foi gravado automaticamente pelo sistema no parâmetro [MV\_ULMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009616322-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-par%C3%A2metro-MV-ULMES). Também pode ser conferido pela rotina MATA220 Saldos Iniciais ou pela tabela SB9 - campo B9\_DATA.

O registro que está tentando movimentar não pode ser originado de data igual ou anterior à data de fechamento do Estoque, gravado nesse campo/parâmetro, do contrário, irá de fato bloquear.

Se de fato for atestado que o movimento é de um período já fechado, a **[Reabertura do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque)**torna-se o caminho contorno mais comum. Porém é sempre importante que se avalie com os setores responsáveis da empresa se é viável a Reabertura do Estoque para que o período ao qual o movimento/documento a ser incluído ou estornado possa ser possível fazê-lo.

**2)** Verifique a data de bloqueio de movimentações no Estoque no parâmetro [MV\_DBLQMOV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-MP-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-durante-o-Fechamento-de-Estoque-).

O registro que está tentando movimentar não pode ser originado de data igual ou anterior à data de bloqueio de movimentos gravada nesse campo/parâmetro, do contrário, irá de fato bloquear.

**3)** Verifique se o movimento que está tentando processar no sistema é originado de uma data anterior ao fechamento, pois nesse caso, será de fato bloqueado.

São considerados na validação, movimentos originados por qualquer rotina no sistema que gere movimento do produto (independente se a TES está configurada para gerar estoque/financeiro). Exemplo: Documento de Entrada (SF1 e SD1), Documento de Saída (SF2 e SD2), Livros Fiscais (SF3), Ordem de Produção PCP (SH6), Movimentos de Estoque (SD3 e SB9), etc. Verificar os campos de data, exemplo: D3\_EMISSAO etc.

**4)** Se o movimento que está tentando realizar envolve Ordem de Produção PCP, verifique o parâmetro [MV\_PRODPR0](https://tdn.totvs.com/pages/releaseview.action?pageId=235593602). Se utilizar este parâmetro com [conteúdo diferente de 3, o sistema permitirá encerrar a OP quando a data base for anterior à data do fechamento](https://tdn.totvs.com.br/pages/releaseview.action?pageId=756473692). Essa configuração precisa ser criteriosamente avaliada conforme a regra de negócio da organização. Tratamento implementado através da MATA250 com data igual ou superior a 03/05/2023. Recomendado aplicar [Expedição contínua do PCP](https://tdn.totvs.com/pages/releaseview.action?pageId=557684117).

**5)** Se o movimento que está tentando realizar envolve i[ntegração com o sistema PIMS](https://tdn.totvs.com/pages/viewpage.action?pageId=223914188) para liberação de Boletim, neste caso, confira se o campo D3\_NRBPIMS está devidamente gravado com o número do boletim [Exemplo de condição no ADAPTER via configurador: *!Empty(SD3->D3\_NRBPIMS)* ]

**6)** Outras possíveis causas / soluções:

**- Ambiente desatualizado, ocasionando incompatibilidade entre as validações.**

Verifique o comportamento em seu ambiente de teste atualizado com o pacote acumulado - Expedição Contínua dos módulos que utiliza, e demais artefatos do ambiente.

[Acumulado SIGAEST](https://tdn.totvs.com/x/2hgdHw) | [LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) ou [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528) ou [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1031460) | Smartclient [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) ou [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1031469) | [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

- **Ambiente sofrendo impacto de customizações (no RPO ou dicionários).**

Verifique o comportamento em seu ambiente de teste padrão (RPO e dicionários) seguindo os [3 métodos indicados nesta orientação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292).

**- Validações realizadas por outro sistema, quando o processo envolve integração com o Protheus.**

Casos onde o processo é realizado em outro sistema, o qual se integra com o sistema Protheus no Estoque, deve ser avaliada também a regra de negócio deste outro sistema. Quais possíveis configurações e validações podem interferir no comportamento do Estoque Protheus. Uma sugestão para isolar a origem do problema é realizar um teste (em ambiente teste padrão e atualizado) incluindo um movimento diretamente no Protheus (por exemplo, um movimento interno com a data atual) e certificar se realmente aparece o mesmo HELP FECHTO, ou se o problema ocorre somente quando o movimento é originado no outro sistema.

**- Inconsistência em registros gravados no banco de dados.**

Já foram notados casos onde há inconsistência de dados no banco, não tendo sido ocasionado por processamento padrão do sistema. Nestes casos, não há atendimento de Suporte ao produto, recomenda-se solicitar um DBA para manutenção na base *[Exemplo: movimento oriundo de integração com outro sistema, no processamento do Protheus o sistema posiciona em registro em branco na tabela SD3, criado porque o de/para na tabela XXF para o código informado, estava  indevidamente deletado na base. Dentre outros exemplos onde há sujeira na base de dados]*. Sujeiras no banco de dados comprometem o correto processamento do sistema.

**Observações complementares:**

- O sistema permite incluir NF de Entrada digitando uma data de emissão (D1\_EMISSAO e D1\_DTDIGIT) anterior à data do parâmetro MV\_ULMES porém, impede a inclusão de NF com a data base do sistema anterior à data do parâmetro MV\_ULMES. Este é um comportamento conceitual, O procedimento esta correto. O sistema bloqueia inclusão de NF com a data base do sistema retroativa a data do parametro MV\_ULMES.

- Caso já tenha realizado todas as validações aqui indicadas, e não identifique a origem do problema, contate o Suporte Técnico mencionando as validações já realizadas conforme esta documentação, e solicite nossa Consultoria do Suporte para investigação em seu ambiente. Teremos prazer em atendê-lo!

**Saiba Mais:**

[SIGAFAT - Exclusão Documento de Saída apresentado: HELP FECHTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042322274-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exclus%C3%A3o-Documento-de-Sa%C3%ADda-apresentado-HELP-FECHTO)

[MV\_CMDBLQV - Controle automático de bloqueio de movimentação durante o Custo Médio e Fechamento de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012892521-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-CMDBLQV-Controle-autom%C3%A1tico-de-bloqueio-de-movimenta%C3%A7%C3%A3o-durante-o-Custo-M%C3%A9dio-e-Fechamento-de-Estoque)

[PEST005 - MV\_PRODPR0 - Custeio da produção](https://tdn.totvs.com/pages/releaseview.action?pageId=6085227)

[Integração PIMS com MV\_PIMSINT desabilitado](https://tdn.totvs.com/pages/viewpage.action?pageId=652852669)
