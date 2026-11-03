---
content_hash: 145522787dea046f4daf5e8ea108e84cb91abce6ec1191275971954c696f360f
fetched_at: '2026-06-29T00:10:35.528312+00:00'
page_id: '531011677'
product: rm
source: tdn-rm
title: LGPD - TOTVS Aprovações e Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531011677
version: 8
---

Nesta página o cliente encontrará os cuidados que deve tomar quanto aos dados pessoais e sensíveis de pessoa natural quanto nas funcionalidades referentes ao TOTVS Aprovações e Atendimento.

**INTEGRAÇÕES:**

Nas integrações da TOTVS ou de terceiros, para implementar segurança a fim de evitar vazamentos de dados pessoais e sensíveis recomendamos a utilização de protocolos seguros.

**INTEGRAÇÕES BANCO A BANCO:**

Nas integrações banco a banco para implementar segurança a fim de evitar vazamentos de dados pessoais e sensíveis, sugerimos o uso de criptografia em ambos os bancos.

No RM as integrações banco a banco podem passar pela intermediação de conceito (TBC), bem como por rotinas totalmente externas feita por terceiros e que implementem integrações direta via banco a banco. Para mais detalhes consulte a Frame do RM e/ou a equipe de DBA RM.

**ROTINAS QUE GERAM ARQUIVOS:**

Para os arquivos gerados em formato txt, xml, csv e outros e que possuam dados pessoais e/ou sensíveis de pessoa natural, sugerimos que após o seu uso seja efetuada a exclusão ou armazenamento definitivo do mesmo em local seguro e forma restrita para que não sejam manipulados por usuários sem a devida permissão e para que não existam vazamentos de dados pessoais e sensíveis.

Um exemplo de rotina que gera arquivo é a exportação dos cadastros disponível nas visões do RM, que pode gerar arquivo nos formatos CSV, XLS, PDF, XLSX, TXT, RTF.

**ENVIO DE E-MAIL:**

No envio de e-mails, a fim de evitar vazamentos de dados pessoais e sensíveis,  sugerimos o uso de protocolos seguros, assim como a disseminação da cultura de segurança em toda a empresa bem como para os destinatários dos e-mails, para que os mesmos protejam suas informações pessoais.

Devem ser verificados ainda as integrações da TOTVS ou de terceiros que podem realizar o envio de e-mail de dados pessoais e sensíveis de pessoa natural,

true

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link** **(<https://tdn.totvs.com/pages/releaseview.action?pageId=514427789>).**
